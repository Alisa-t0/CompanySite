from django.forms import ModelForm, NumberInput, TelInput, TextInput, DateInput, CheckboxInput
from django.shortcuts import render

from main.models import Worker


class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = [ 'name', 'surname', 'position', 'salary', 'phone', 'date_hired', 'is_active']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'surname': TextInput(attrs={'class': 'form-control'}),
            'position': TextInput(attrs={'class': 'form-control'}),
            'salary': NumberInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control'}),
            'date_hired': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_active': CheckboxInput(attrs={'class': 'form-control'}),
        }