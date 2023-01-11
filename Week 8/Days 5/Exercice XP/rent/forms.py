from django import forms
from django.forms import ModelForm
from .models import Customer
from .models import Location
from .models import Vehicule
from .models import TypeVehicule
from .models import Tarif_location
from .models import TailleVehicule
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


class TypeForm(ModelForm):
    class Meta:
        model = TypeVehicule
        fields = '__all__'


class TailleForm(ModelForm):
    class Meta:
        model = TailleVehicule
        fields = '__all__'


class TarifForm(ModelForm):
    class Meta:
        model = Tarif_location
        fields = '__all__'