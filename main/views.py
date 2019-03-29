from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

import re

from main.models import CardIndex, Client

# Create your views here.
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
    if request.method == 'POST' and request.POST['search']:
        query = request.POST['search'].strip()
        if query.isdigit():
            search = CardIndex.objects.filter(ipd = query)
        else:
            split = str(query).split()
            search = Client.objects.filter(last_name=split[0].title(), first_name=split[1].title(), middle_name=split[2].title())
        #return HttpResponse(serializers.serialize('json', search), content_type="application/json")
        return render(request, 'main/archiv.html', {'data_search': search})
    else:
        return render(request, 'main/archiv.html')


def ajax_search(request):
    """ Поиск пациентов """
    objects = []
    if request.method == "GET" and request.GET['query'] and request.GET[
        'type']:  # Проверка типа запроса и наличия полей
        type = request.GET['type']
        query = request.GET['query'].strip()
        p = re.compile(r'[а-я]{3}[0-9]{8}',
                       re.IGNORECASE)  # Регулярное выражение для определения запроса вида иии10121999
        p2 = re.compile(
            r'([А-я]{2,}) ([А-я]{2,}) ([А-я]{0,}) ([0-9]{2}.[0-9]{2}.[0-9]{4})')  # Регулярное выражение для определения запроса вида Иванов Иван Иванович 10.12.1999
        p3 = re.compile(r'[0-9]{1,10}')  # Регулярное выражение для определения запроса по номеру карты
        if re.search(p, query):  # Если это краткий запрос
            initials = query[0:3]
            btday = query[3:5] + "." + query[5:7] + "." + query[7:11] + " 0:00:00"
            if type == "all":
                objects = Importedclients.objects.filter(initials=initials, birthday=btday)[0:10]
            else:
                objects = Importedclients.objects.filter(initials=initials, birthday=btday, type=type)[0:10]
        elif re.search(p2, query):  # Если это полный запрос
            split = str(query).split()
            btday = split[3] + " 0:00:00"
            if type == "all":  # Проверка типа базы, all - поиск по Поликлиннике и по Стационару
                objects = Importedclients.objects.filter(family=split[0], name=split[1], twoname=split[2],
                                                         birthday=btday)[0:10]
            else:
                objects = Importedclients.objects.filter(family=split[0], name=split[1], twoname=split[2],
                                                         birthday=btday, type=type)[0:10]
        elif re.search(p3, query):  # Если это запрос номер карты
            try:
                objects = Importedclients.objects.filter(num=int(query), type=type)[0:10]
            except ValueError:
                pass
    return HttpResponse(serializers.serialize('json', objects), content_type="application/json")  # Создание JSON