from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название книги")
    description = models.TextField(verbose_name="Описание книги")
    left = models.PositiveIntegerField(verbose_name="Книг на складе")
    image = models.ImageField(verbose_name="Обложка книги")

    def get_abolute_url(self):
        return reverse("main_page:book", kwargs={'idx': self.pk})
