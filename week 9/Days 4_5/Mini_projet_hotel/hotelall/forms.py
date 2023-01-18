from django.forms import ModelForm, Form
from .models import *
from django import forms

class ReserverForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields ='__all__'

class ChambreForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields ='__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'




