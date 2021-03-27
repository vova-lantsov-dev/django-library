from django.contrib import admin
from django.urls import path
from .views import main, book_page, thanks

app_name = "main_page"

urlpatterns = [
    path('', main, name='main'),
    path('book/<int:idx>/', book_page, name='book'),
    path('thanks/', thanks, name='thanks'),
]
