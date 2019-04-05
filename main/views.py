from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

import re

from main.models import CardIndex, Client, Control
from users.models import UsersProfile, User
from main.forms import *
from main.decorators import group_required

# Create your views here.
def index(request):
    """"""
    return render(request, 'main/index.html')

@login_required
def main(request):
    """Домашняя страница картотеки"""
    menu = []
    groups = [str(x) for x in request.user.groups.all()]
    if request.user.is_superuser:
        return render(request, 'main/admin.html')
    if "Архивариус" in groups:
        return render(request, 'main/archiv.html')
    if "Специалист" in groups:
        return render(request, 'main/spec.html')

@login_required
def search(request):
    '''Поиск информации по базе данных для архивариуса'''
    groups = [str(x) for x in request.user.groups.all()]
    con = Control.objects.all()
    spec = UsersProfile.objects.all()
    if request.method == 'POST' and request.POST['search']:
        query = request.POST['search'].strip()
        if query.isdigit():
            search = CardIndex.objects.filter(ipd = query)
        else:
            split = str(query).split()
            search = CardIndex.objects.filter(client__last_name=split[0].title(),
                                              client__first_name=split[1].title(),
                                              client__middle_name=split[2].title())
        if "Архивариус" in groups:
            return render(request, 'main/archiv.html', {'data_search': search, 'control': con, 'spec': spec})
        if "Специалист" in groups:
            return render(request, 'main/spec.html', {'data_search': search, 'control': con, 'spec': spec})
    else:
        return render(request, 'main/index.html')

@login_required
@group_required("Архивариус")
def ld(request, ld_id):
    """Выводит одну тему и все ее записи."""
    data = CardIndex.objects.get(id=ld_id)
    context = {'ld': data}
    return render(request, 'main/ld.html', context)

@login_required
@group_required("Архивариус")
def edit_ld(request, ld_id):
    """Редактирует существующую запись."""
    ld = CardIndex.objects.get(id=ld_id)
    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей записи.
        form = AddLdForm(instance=ld)
    else:
        # Отправка данных POST; обработать данные.
        form = AddLdForm(instance=ld, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:ld', args=[ld.id]))
    context = {'ld': ld, 'form': form}
    return render(request, 'main/editld.html', context)

@login_required
def ldinjob(request):
    """Выводит личные дела в работе специалиста"""
    injob = CardIndex.objects.filter(spec=request.user.usersprofile).order_by('ipd')
    return render(request, 'main/injob.html', {'injob': injob})

@login_required
@group_required("Архивариус")
def newld(request):
    """Добавление нового ЛД"""
    if request.method != 'POST':
        form = AddLdForm()
    else:
        form = AddLdForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:main'))

    context = {'form': form}
    return render(request, 'main/newld.html', context)


@login_required
@group_required("Архивариус")
def newclient(request):
    """Добавление нового клиента"""
    if request.method != 'POST':
        form = AddClientForm()
    else:
        form = AddClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:main'))
    context = {'form': form}
    return render(request, 'main/newclient.html', context)


def queryld(request):
    '''Функция запроса ЛД'''
    if request.method != 'POST':
        form = AddQueryLdForm()
    else:
        form = AddQueryLdForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:main'))
    context = {'form': form}
    return render(request, 'main/queryld.html', context)
