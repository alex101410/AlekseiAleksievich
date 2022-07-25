from tabnanny import verbose
from turtle import title
from django.db import models

class Product (models.Model):
    brend = models.TextField(
        verbose_name='Бренд',
    )
    article = models.TextField(
        verbose_name='Артикл',
    )
    quantity = models.TextField(
        verbose_name='Количество',
    )
    cost = models.DecimalField(
        verbose_name='Цена', max_digits=5, decimal_places=2,
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
