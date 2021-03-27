from django.db import models
from main.models import Book


class Customer(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя заказчика")
    email = models.EmailField(max_length=150, verbose_name="Почта заказчика")
    phone = models.IntegerField(verbose_name="Номер телефона заказчика")
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.CASCADE)
