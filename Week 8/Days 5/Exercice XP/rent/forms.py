from django import forms
from django.forms import ModelForm
from .models import Customer
from .models import Location
from .models import Vehicule
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'



class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class VehiculeForm(ModelForm):
    class Meta:
        model = Vehicule
        fields = '__all__'
