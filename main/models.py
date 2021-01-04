from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Consumption(models.Model):
    # Пользователь, который этот расход совершил
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, default='Без имени')

    CATEGORIES = (
        ('property', 'Недвижимость'),
        ('health', 'Здоровье'),
        ('presents', 'Подарки'),
        ('travel', 'Поездки'),
        ('personal', 'Личные расходы'),
        ('clothes', 'Одежда'),
        ('food', 'Питание'),
        ('help', 'Помощь'),
        ('personal_transport', 'Личный транспорт'),
        ('public_transport', 'Общественный транспорт'),
        ('other', 'Другое'),
    )

    category = models.CharField(
        choices=CATEGORIES, max_length=100, default='other')
    date = models.DateTimeField(default=datetime.now(), editable=True)
    amount = models.FloatField()  # Расход в валюте

    SCORES = (
        (0, '0'), (1, '1'), (2, '2'),
        (3, '3'), (4, '4'), (5, '5'),
        (6, '6'), (7, '7'), (8, '8'),
        (9, '9'), (10, '10'),
    )

    rating = models.PositiveSmallIntegerField(choices=SCORES) # Оценка целесообразности расхода (от 0 до 10)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'

    def __str__(self):
        return '{0: .2f} р., {1}, Категория: {2}'.format(self.amount, self.name, self.category)
