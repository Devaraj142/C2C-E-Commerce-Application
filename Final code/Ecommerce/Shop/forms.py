from django import forms
from .models import Sales, Service

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['product','name', 'image', 'price','mobilenum']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['oname','address','phnum','district','pin','pname','mname','defect']
        