"""Определяет схемы URL для MAIN."""

from django.conf.urls import url
from . import views

urlpatterns = [
    # Домашняя страница
    url(r'^$', views.main, name='main'),
    url(r'^archiv$', views.search, name='search'),
    url(r'^archiv/(?P<ld_id>\d+)/$', views.ld, name='ld'),
    url(r'editld/(?P<ld_id>\d+)/$', views.edit_ld, name='edit_ld'),
    url(r'^injob$', views.ldinjob, name='ldinjob'),
]