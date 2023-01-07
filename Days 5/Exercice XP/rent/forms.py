from django import  forms
from .models import Customer
from .models import Location
from .models import Vehicule
class CustomerForm(forms.Form):
    class Meta:
        model = Customer
        fields = '__all__'



class LocationForm(forms.Form):
    class Meta:
        modele = Location
        fields = '__all__'


class VehiculeForm(forms.Form):
    class Meta:
        modele = Vehicule
        fields = '__all__'
