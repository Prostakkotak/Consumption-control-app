from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

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

class Consumption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # Пользователь, который этот расход совершил
    name = models.CharField(max_length=100, default='Без имени') 
    category = models.CharField(choices=CATEGORIES, max_length=100, default='other')
    date = models.DateTimeField(default=datetime.now(), editable=True)
    amount = models.FloatField() # Расход в валюте
    rating = models.PositiveSmallIntegerField() # Оценка целесообразности расхода (от 0 до 10)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'

    def __str__(self):
        return '{0: .2f}, {1}, Категория: {2}'.format(self.amount, self.name, self.category)