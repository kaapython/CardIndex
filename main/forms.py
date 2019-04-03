from django import forms
from main.models import *

class AddLdForm(forms.ModelForm):
    class Meta:
        model = CardIndex
        fields = [
            'ipd',
            'client',
            'control',
            'category',
            'spec',
            'info',
        ]
        labels = {
            'client': 'Клиент',
            'control': 'Статус',
            'category': 'Категория',
            'ipd': 'ИПД',
            'info': 'Движение ЛД',
            'spec': 'ФИО специалиста'
        }

class EditLdForm(forms.ModelForm):
    class Meta:
        model = CardIndex
        fields = ['client']
        labels = {'client': ''}
        widgets = {'client': forms.Textarea(attrs={'cols': 40})}