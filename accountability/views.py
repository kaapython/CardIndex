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

    if tp == "ld":
        lds = CardIndex.objects.all()
        response['Content-Disposition'] = str.translate(
            "attachment; filename='Отчет по количеству действующих ЛД.xls'".format(), tr)
        ws = wb.add_sheet('Всего ЛД')

        font_style_wrap = xlwt.XFStyle()
        font_style_wrap.alignment.wrap = 1
        font_style_wrap.borders = borders
        font_style = xlwt.XFStyle()
        font_style.borders = borders

        row_i = 0
        row = [
            ('ИПД', 4000),
            ('ФИО', 7000),
            ('Контроль', 5000),
            ('Специалист', 9000),
        ]

        for i in range(len(row)):
            ws.write(row_i, i, row[i][0])
            ws.col(i).width = row[i][1]

        row_i = 1

        for ld in lds:
            row = [
                str(ld.ipd),
                str(ld.client),
                str(ld.control),
                str(ld.spec)
            ]
            for i in range(len(row)):
                ws.write(row_i, i, row[i])
            row_i += 1


    wb.save(response)
    return response