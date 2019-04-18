from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from main.views import *
from users.views import *

# Create your views here.

def accountability(request):
    '''Формирование отчетов'''
    lds = CardIndex.objects.all()
    querys = Query.objects.all()
    return render(request, 'accountability/accountability.html', {'lds': lds, 'querys': querys})

@csrf_exempt
@login_required
def statistic_xls(request):
    """ Генерация отчетов в формате XLS """
    import xlwt

    wb = xlwt.Workbook(encoding='utf-8')
    response = HttpResponse(content_type='application/ms-excel')

    if request.method == "POST":
        pk = request.POST["pk"]  # Первичный ключ
        tp = request.POST["type"]  # Тип статистики

    else:
        pk = request.GET["pk"]  # Первичный ключ
        tp = request.GET["type"]  # Тип статистики

    symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
               u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")  # Словарь для транслитерации
    tr = {ord(a): ord(b) for a, b in zip(*symbols)}  # Перевод словаря для транслита

    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN

    if tp == "all_ld":
        # Формирование отчетов по всем ЛД для архивариуса

        lds = CardIndex.objects.all()
        response['Content-Disposition'] = str.translate(
            "attachment; filename='Отчет по количеству действующих ЛД.xls'".format(), tr)
        ws = wb.add_sheet('Всего ЛД в картотеке')

        font_style_wrap = xlwt.XFStyle()
        font_style_wrap.alignment.wrap = 1
        font_style_wrap.borders = borders
        font_style = xlwt.XFStyle()
        font_style.borders = borders

        row_i = 0
        row = [
            ('ИПД', 4000),
            ('ФИО', 7000),
            ('Контроль', 5500),
            ('Специалист', 9000),
        ]

        for i in range(len(row)):
            ws.write(row_i, i, row[i][0], font_style_wrap)
            ws.col(i).width = row[i][1]

        row_i = 1

        for ld in lds:
            if ld.spec == None:
                row = [
                    str(ld.ipd),
                    str(ld.client),
                    str(ld.control),
                    'не назначен'
                ]
            else:
                row = [
                    str(ld.ipd),
                    str(ld.client),
                    str(ld.control),
                    str(ld.spec)
                ]
            for i in range(len(row)):
                ws.write(row_i, i, row[i], font_style_wrap)
            row_i += 1

    if tp == "spec":
        # Формирование отчетов по специалистам

        specs = CardIndex.objects.filter(spec=pk)
        response['Content-Disposition'] = str.translate(
            "attachment; filename='Отчет по специалисту.xls'".format(), tr)


        ws = wb.add_sheet("ЛД в работе")

        font_style_wrap = xlwt.XFStyle()
        font_style_wrap.alignment.wrap = 1
        font_style_wrap.borders = borders
        font_style = xlwt.XFStyle()
        font_style.borders = borders
        row_i = 0
        row = [
            ('ИПД', 4000),
            ('ФИО', 7000),
            ('Адрес', 10000),
            ('Статус', 5500),
            ('Специалист', 9000),
        ]

        for i in range(len(row)):
            ws.write(row_i, i, row[i][0], font_style_wrap)
            ws.col(i).width = row[i][1]

        row_i += 1

        for s in specs:
            row_s = [
                str(s.ipd),
                str(s.client),
                str(s.client.address),
                str(s.category),
                str(s.spec),
            ]
            for i in range(len(row_s)):
                ws.write(row_i, i, row_s[i], font_style_wrap)
            row_i += 1

    if tp == "archiv":
        # Формирование отчетов находищихся в архиве

        archiv = CardIndex.objects.filter(control__id=6)
        response['Content-Disposition'] = str.translate(
            "attachment; filename='Отчет ЛД находящихся в архиве.xls'".format(), tr)


        ws = wb.add_sheet("ЛД в архиве")

        font_style_wrap = xlwt.XFStyle()
        font_style_wrap.alignment.wrap = 1
        font_style_wrap.borders = borders
        font_style = xlwt.XFStyle()
        font_style.borders = borders
        row_i = 0
        row = [
            ('ИПД', 4000),
            ('ФИО', 7000),
            ('Адрес', 10000),
            ('Статус', 5500),
            ('Движение ЛД', 4000),
        ]

        for i in range(len(row)):
            ws.write(row_i, i, row[i][0], font_style_wrap)
            ws.col(i).width = row[i][1]

        row_i += 1

        for arch in archiv:
            row_s = [
                str(arch.ipd),
                str(arch.client),
                str(arch.client.address),
                str(arch.category),
                str(arch.control),
            ]
            for i in range(len(row_s)):
                ws.write(row_i, i, row_s[i], font_style_wrap)
            row_i += 1

    if tp == "offsite":
        # Формирование отчетов находящихся в др. уч.

        offsite = CardIndex.objects.filter(control__id=3)
        response['Content-Disposition'] = str.translate(
            "attachment; filename='Отчет ЛД находящихся в других учреждениях.xls'".format(), tr)


        ws = wb.add_sheet("ЛД в др. уч.")

        font_style_wrap = xlwt.XFStyle()
        font_style_wrap.alignment.wrap = 1
        font_style_wrap.borders = borders
        font_style = xlwt.XFStyle()
        font_style.borders = borders
        row_i = 0
        row = [
            ('ИПД', 4000),
            ('ФИО', 7000),
            ('Адрес', 10000),
            ('Статус', 5500),
            ('Движение ЛД', 5000),
        ]

        for i in range(len(row)):
            ws.write(row_i, i, row[i][0], font_style_wrap)
            ws.col(i).width = row[i][1]

        row_i += 1

        for off in offsite:
            row_s = [
                str(off.ipd),
                str(off.client),
                str(off.client.address),
                str(off.category),
                str(off.control),
            ]
            for i in range(len(row_s)):
                ws.write(row_i, i, row_s[i], font_style_wrap)
            row_i += 1

    wb.save(response)
    return response