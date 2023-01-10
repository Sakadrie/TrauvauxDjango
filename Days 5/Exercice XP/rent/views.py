from django.shortcuts import render, redirect
from .models import Location
from .models import Vehicule
from .models import TailleVehicule
from .models import TypeVehicule
from .models import Tarif_location
from .models import Customer
from .forms import CustomerForm
from .forms import VehiculeForm
from .forms import LocationForm
from faker import Faker
# Create your views here.

def index(request):
    return render(request, "rent/index.html")

def rental(request):
    rentals = Location.objects.all()
    context = {
         "rentals": rentals
    }
    return render(request, "rent/rental.html", context)


def rentals(request, id):
    rentals= Location.objects.get(id=id)
    return render(request, "rent/rental.html",  {"rentals": rentals})


def rental_add(request):
    if request.method == 'POST':
        # On initialise le formulaire avec les données contenues
        form = LocationForm(request.POST)
        # test si le formulaire est valide
        if form.is_valid():
            # On enregistre
            form.save()
            return redirect("rental")
    else:
        # si non on initialise un formualire vide
        form = LocationForm()
    return render(request, 'rent/addlocation.html', {"form": form})


def customer(request):
    client = Customer.objects.all()
    return render(request, "rent/customer.html", {"customer": client})



def customers(request, id):
    customers= Customer.objects.get(id=id)
    return render(request, 'rent/vehicule.html', {"customers": customers})
    pass


def customer_add(request):
    if request.method == 'POST':
        # On initialise le formulaire avec les données contenues
        form = CustomerForm(request.POST)
        # test si le formulaire est valide
        if form.is_valid():
            # On enregistre
            form.save()
            return redirect("customer")
    else:
        # si non on initialise un formualire vide
        form = CustomerForm()
    return render(request, 'rent/addclient.html', {"form": form})


def vehicule(request):
    vehicule = Vehicule.objects.all()
    return render(request, 'rent/vehicule.html', {"vehicule": vehicule})


def vehicules(request, id):
    vehicules = Vehicule.objects.get(id=id)
    return render(request, 'rent/vehicule.html', {"vehicules": vehicules})



def vehicule_add(request):
    if request.method == 'POST':
        # On initialise le formulaire avec les données contenues
        form = VehiculeForm(request.POST)
        # test si le formulaire est valide
        if form.is_valid():
            # On enregistre
            form.save()
            return redirect("vehicule")
    else:
        # si non on initialise un formualire vide
        form = VehiculeForm()
    return render(request, 'rent/addvehicule.html', {"form": form})


def generate_faker(request):
    fake = Faker()
    for x in range(30):
        customer = Customer(
            nom=fake.first_name(),
            prenom=fake.last_name(),
            email=fake.email(),
            phonenumber=fake.phone_number(),
            adresse=fake.address(),
            ville=fake.city(),
            pays=fake.country()
        )
        customer.save()
        return redirect("customer")