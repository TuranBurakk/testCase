from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'id' : 'ID',
            'name': 'İsim',
            'surname': 'Soyisim',
            'tc_no': 'TC Kimlik No',
            'phone': 'Telefon',
            'city': 'Şehir',
            'district': 'İlçe',
        }
        
    