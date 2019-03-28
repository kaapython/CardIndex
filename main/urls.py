"""Определяет схемы URL для MAIN."""

from django.conf.urls import url
from . import views

urlpatterns = [
    # Домашняя страница
    url(r'^$', views.main, name='main'),
]