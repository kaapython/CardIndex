from django.shortcuts import render

# Create your views here.

def index(request):
    """Домашняя страница картотеки"""
    return render(request, 'main/index.html')