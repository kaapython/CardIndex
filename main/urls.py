"""Определяет схемы URL для MAIN."""

from django.conf.urls import url
from . import views
from accountability.views import statistic_xls as statistic_xls

urlpatterns = [
    # Домашняя страница
    url(r'^$', views.main, name='main'),
    url(r'^index$', views.index, name='index'),
    url(r'^archiv$', views.search, name='search'),
    url(r'^archiv/(?P<ld_id>\d+)/$', views.ld, name='ld'),
    url(r'editld/(?P<ld_id>\d+)/$', views.edit_ld, name='edit_ld'),
    url(r'^injob$', views.ldinjob, name='ldinjob'),
    url(r'^newld$', views.newld, name='newld'),
    url(r'^newclient$', views.newclient, name='newclient'),
    url(r'^queryld$', views.queryld, name='queryld'),
    url(r'^archiv_querys$', views.archiv_querys, name='archiv_querys'),
    url(r'^statistic_xls', statistic_xls, name='statistic_xls'),

]