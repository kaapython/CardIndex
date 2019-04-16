"""Определяет схемы URL для Accountability."""

from django.conf.urls import url
from . import views


urlpatterns = [
    # Страница отчетности
    url(r'^accountability', views.accountability, name='accountability'),
    url(r'^statistic_xls', views.statistic_xls, name='statistic_xls'),
]
