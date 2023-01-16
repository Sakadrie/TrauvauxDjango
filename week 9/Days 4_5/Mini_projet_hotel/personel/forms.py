
from django.forms import ModelForm, Form
from .models import Customer
from .models import Reservation

class ReserverForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

