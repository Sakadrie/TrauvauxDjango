from django.shortcuts import render, redirect
from .models import Location
from .models import Vehicule
from .models import TailleVehicule
from .models import TypeVehicule
from .models import Tarif_location
from .models import Customer
from .forms import CustomerForm
from .forms import VehiculeForm
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
    pass


def rental_add(request):
    pass


def customer(request):
    client = Customer.objects.all()
    return render(request, "rent/customer.html", {"customer": client})



def customers(request, id):
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
    return render(request, 'rent/addvehicule.html', {"form2": form})

