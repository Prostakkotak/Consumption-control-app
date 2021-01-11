from django.shortcuts import render, get_object_or_404, Http404, redirect
from django.views.generic import View

# Импорт моделей
from .models import *

# Импорт форм
from .forms import *

# Импорты для системы аутентификации
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Импорты для разнообразного функционала
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, timedelta


class Index(View):
    def get(self, request):

        if request.user.is_authenticated:
            consumption_list = Consumption.objects.filter(user=request.user)

            if len(consumption_list) == 0:
                return render(request, 'main/index.html', context={'zero_consumptions': 1})

            '''Расчет суммы расходов за последние 24 часа'''
            consumption_amount_24h = 0  # Переменная для хранения суммы

            # Цикл по экземплярам модели не старше 24 часов
            for consumption in consumption_list.exclude(date__lt=datetime.now() - timedelta(hours=24)):
                consumption_amount_24h += consumption.amount  # Суммирование расходов

            return render(request, 'main/index.html', context={
                'last_consumption': consumption_list[0],
                'last_10_consumption': consumption_list[:10],
                'consumption_amount_24h': consumption_amount_24h,
            })

        return render(request, 'main/index.html')


class MonthlyReport(View):
    def get(self, request):

        if request.user.is_authenticated:

            consumption_list = Consumption.objects.filter(user=request.user)

            if len(consumption_list) == 0:
                return render(request, 'main/index.html', context={'zero_consumptions': 1})

            '''Расчет суммы расходов и эффективности трат за последние 30 дней'''
            consumption_list_30d = consumption_list.exclude(
                date__lt=datetime.now() - timedelta(days=30))

            consumption_amount_30d = 0  # Переменная для хранения суммы расходов
            efficiency_sum = 0  # Переменная для хранения суммы целесообразности расходов
            consumption_count = len(consumption_list_30d)  # Кол-во расходов

            for consumption in consumption_list_30d:  # Цикл по экземплярам модели
                consumption_amount_30d += consumption.amount  # Суммирование расходов
                efficiency_sum += consumption.rating

            # Расчет эффективности трат
            efficiency_score = round((efficiency_sum / (consumption_count * 10)) * 10, 2)

            categories = [  # Список категорий для расчета процентного соотношения для диаграммы
                'property',
                'health',
                'presents',
                'travel',
                'personal',
                'clothes',
                'food',
                'help',
                'personal_transport',
                'public_transport',
                'other',
            ]

            categories_ru = [
                'Недвижимость',
                'Здоровье',
                'Подарки',
                'Поездки',
                'Личные расходы',
                'Одежда',
                'Еда',
                'Помощь',
                'Личный транспорт',
                'Общественный транспорт',
                'Другое',
            ]

            percents = []
            i = 0

            for category in categories:
                temp_list = consumption_list_30d.filter(category=category)
                category_sum = 0

                for consumption in temp_list:
                    category_sum += consumption.amount

                percents.append(float('{0: .1f}'.format(
                    (category_sum / consumption_amount_30d) * 100)))

                categories[i] += '{0: .1f}'.format(
                    (category_sum / consumption_amount_30d) * 100)
                categories_ru[i] += '{0: .1f}'.format(
                    (category_sum / consumption_amount_30d) * 100)

                i += 1

            return render(request, 'main/report.html', context={
                'consumption_amount_30d': consumption_amount_30d,
                'efficiency_score': efficiency_score,
                'percents': percents,
                'categories': categories,
                'categories_ru': categories_ru,
            })

        return redirect('index')


class FullReport(View):
    def get(self, request):

        if request.user.is_authenticated:

            consumption_list = Consumption.objects.filter(user=request.user)

            if len(consumption_list) == 0:
                return render(request, 'main/index.html', context={'zero_consumptions': 1})

            consumption_amount = 0  # Переменная для хранения суммы расходов
            efficiency_sum = 0  # Переменная для хранения суммы целесообразности расходов
            consumption_count = len(consumption_list)  # Кол-во расходов

            for consumption in consumption_list:  # Цикл по экземплярам модели
                consumption_amount += consumption.amount  # Суммирование расходов
                efficiency_sum += consumption.rating

            # Расчет эффективности трат
            efficiency_score = round((efficiency_sum / (consumption_count * 10)) * 10, 2)

            categories = [  # Список категорий для расчета процентного соотношения для диаграммы
                'property',
                'health',
                'presents',
                'travel',
                'personal',
                'clothes',
                'food',
                'help',
                'personal_transport',
                'public_transport',
                'other',
            ]

            categories_ru = [
                'Недвижимость',
                'Здоровье',
                'Подарки',
                'Поездки',
                'Личные расходы',
                'Одежда',
                'Еда',
                'Помощь',
                'Личный транспорт',
                'Общественный транспорт',
                'Другое',
            ]

            percents = []
            i = 0

            for category in categories:
                temp_list = consumption_list.filter(category=category)
                category_sum = 0

                for consumption in temp_list:
                    category_sum += consumption.amount

                percents.append(float('{0: .1f}'.format(
                    (category_sum / consumption_amount) * 100)))

                categories[i] += '{0: .1f}'.format(
                    (category_sum / consumption_amount) * 100)
                categories_ru[i] += '{0: .1f}'.format(
                    (category_sum / consumption_amount) * 100)

                i += 1

            return render(request, 'main/full_report.html', context={
                'consumption_amount': consumption_amount,
                'efficiency_score': efficiency_score,
                'percents': percents,
                'categories': categories,
                'categories_ru': categories_ru,
            })

        return redirect('index')


class CreateConsumption(View):
    create_form = ConsumptionForm
    model = Consumption

    def get(self, request):

        if request.user.is_authenticated:
            context = {}

            form = self.create_form()

            context.update({
                'form': form,
            })

            return render(request, 'main/create_consumption.html', context)
        else:
            return redirect('index')

    def post(self, request):
        form = self.create_form(request.POST)

        if form.is_valid() and request.user.is_authenticated:
            created_model = form.save()

            try:
                created_model.user = request.user
            except AttributeError:
                pass

            created_model.date = datetime.now()
            created_model.save()

            return redirect('index')
        else:
            messages.warning(request, 'Check your form')
            return redirect('index')


class DeleteConsumption(View):
    model = Consumption

    def get(self, request, pk):
        if request.user.is_authenticated:
            deleting_model = get_object_or_404(self.model, pk=pk)
            deleting_model.delete()

            if request.GET.get('next'):
                return redirect(request.GET.get('next'))

            return redirect('index')


class Registration(View):
    def get(self, request):
        form = UserCreationForm()

        return render(request, 'registration/registration.html', context={
            'form': form,
        })

    def post(self, request):
        form = UserCreationForm(data=request.POST or None)

        if form.is_valid():
            u_name = form.cleaned_data.get('username')
            u_pass = form.cleaned_data.get('password2')

            form.save()

            user = authenticate(
                username=u_name,
                password=u_pass
            )

            # Логиним пользователя после успешной регистрации
            login(request, user)

            return redirect('index')

        return render(request, 'registration/registration.html', context={
            'form': form,
        })
