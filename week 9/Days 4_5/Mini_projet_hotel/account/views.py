from django.shortcuts import render, redirect
from . import forms
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from .models import User
# Create your views here.

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('index1')
        message = 'Indentification Invalides.'
    return render(request, 'account/login.html', context={'form': form, 'message': message})

def logout_user(request):
    logout(request)
    return redirect('login_page')

def register(request):
    #crée une instance du formulaire
    form = forms.RegisterForm()
    #Test l'action si post (envoi de donnée)
    if request.method == 'POST':
        # On recupère les données dans l'instance du formulaire
        form = forms.RegisterForm(request.POST, request.FILES)
        #Verifie si le formulaire est valide
        if form.is_valid():
            #sauvegarde
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'account/inscrire.html', context={'form': form})



def users(request):
    user_all = User.objects.all()
    return render(request, 'account/users.html', {"user_all":user_all})

