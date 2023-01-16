from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from phonenumber_field.modelfields import PhoneNumberField
class LoginForm(forms.Form):
    username = forms.CharField(max_length=70, label="Nom d'Utilisateur")
    password = forms.CharField(max_length=70, widget=forms.PasswordInput, label="Mot de passe")

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'role', 'profile_photo')