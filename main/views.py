from django.shortcuts import render, get_object_or_404, Http404, redirect
from django.views.generic import View

# Импорт моделей
from .models import *

# Импорты для системы аутентификации
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Импорты для разнообразного функционала
from django.contrib import messages
from django.utils import timezone

class Index(View):
    def get(self, request):
        return render(request, 'main/index.html')

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