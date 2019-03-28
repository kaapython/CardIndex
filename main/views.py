from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
    if request.method == 'POST':
        search = CardIndex.objects.filter(ipd = request.POST['search'])
        return render(request, 'main/archiv.html', {'data_search': search})
    else:
        return render(request, 'main/archiv.html')