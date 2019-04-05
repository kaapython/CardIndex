from django import forms
from main.models import *

class AddControl(forms.ModelForm):
    class Meta:
        model = Control
        fields = [
            'check_mark',
        ]

        labels = {
            'check_mark': ''
        }

class AddCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'category',
        ]

        labels = {
            'category': ''
        }

class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'last_name',
            'first_name',
            'middle_name',
            'bday',
            'address'

        ]
        labels = {
            'last_name': '',
            'first_name': '',
            'middle_name': '',
            'bday': '',
            'address': ''
        }


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
            'client': '',
            'control': '',
            'category': '',
            'ipd': '',
            'info': '',
            'spec': ''
        }

class AddQueryLdForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = [
            'query_client',
            'query_date',
            'query_ld',
            'query_spec'
        ]

        labels = {
            'query_client': '',
            'query_date': '',
            'query_ld': '',
            'query_spec': ''
        }

class EditLdForm(forms.ModelForm):
    class Meta:
        model = CardIndex
        fields = ['client']
        labels = {'client': ''}
        widgets = {'client': forms.Textarea(attrs={'cols': 50})}


