from django.forms import ModelForm, Form
from .models import Reservation
from .models import Message

class ReserverForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

class MessageForm(Form):
    class Meta:
        model = Message
        fields = '__all__'