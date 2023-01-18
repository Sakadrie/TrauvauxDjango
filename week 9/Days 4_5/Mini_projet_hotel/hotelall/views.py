
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerForm
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'personel/dashboard.html')

def home(request):
    return render(request, 'visitor/index.html')


def users(request):
    client = Customer.objects.all()
    return render(request, 'personel/customer.html', {'client': client})

def customer_add(request):
    if request.method == 'POST':
        # on initialise le formulaire avec
        form = CustomerForm(request.POST)
        # test si le formulaire est valide
        if form.is_valid():
            form.save()
            form = CustomerForm()
    else:
        form = CustomerForm()
    return render(request, 'personel/addclient.html', {"form": form})


def reservation(request):
    reservation = Reservation.objects.all()
    return render(request, 'personel/reserver.html', {"reservation": reservation})


def rental_add(request):
    if request.method == 'POST':
        # On initialise le formulaire avec les données contenues
        form = ReserverForm(request.POST)
        # test si le formulaire est valide
        if form.is_valid():
            # On enregistre
            form.save()
            return redirect("reservation")
    else:
        # si non on initialise un formualire vide
        form = ReserverForm()
    return render(request, 'personel/addreser.html', {"form": form})



def chambres(request):
    chambre = Chambre.objects.all()
    return render(request, 'personel/chambre.html', {"chambre": chambre})


def add_chambre(request):
    if request.method == 'POST':
        # On initialise le formulaire avec les données contenues
        form = ChambreForm(request.POST)
        # test si le formulaire est valide
        if form.is_valid():
            # On enregistre
            form.save()
            return redirect("rental")
    else:
        # si non on initialise un formualire vide
        form = ChambreForm()
    return render(request, 'personel/addchambre.html', {"form": form})


def message(request):
    mess = Avis.objects.all()
    return render(request, 'personel/read.html', {'avis':mess})

def add_message(request):
    if request.method == 'POST':
        # On initialise le formulaire avec les données contenues
        form = ChambreForm(request.POST)
        # test si le formulaire est valide
        if form.is_valid():
            # On enregistre
            form.save()
            return redirect("rental")
    else:
        # si non on initialise un formualire vide
        form = ChambreForm()
    return render(request, 'visitor/index.html', {"form": form})


def del_sms(request, id):
    sms = Avis.objects.get(id=id)
    if request.method == 'POST':
        sms.delete()
        return redirect("reservation")
    return render(request, "rent/delete.html", {"sms": sms})


def delete(request, id):
    rental = Reservation.objects.get(id=id)
    if request.method == 'POST':
        rental.delete()
        return redirect("reservation")
    return render(request, "rent/delete.html", {"reservation": rental})
