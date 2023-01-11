from django.contrib import messages
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
from .forms import TypeForm
from .forms import TarifForm
from .forms import TailleForm
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
    return render(request, "rent/detailsloc.html",  {"rentals": rentals})


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
    customers = Customer.objects.get(id=id)
    return render(request, 'rent/detailsloc.html', {"customer": customers})


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
    return render(request, 'rent/detailsloc.html', {"vehicules": vehicules})



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



def delete(request, id):
    client = Customer.objects.get(id=id)
    if request.method == 'POST':
        client.delete()
        return redirect("customer")
    return render(request, "rent/delete.html", {"customer": client})


def update(request, id):
    client = Customer.objects.get(id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=client)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"successfully {client.nom} was edited !")
            return redirect('customer')
        else:
            form = CustomerForm(instance=client)
        return render(request, 'rent/update.html', {'form': form})


def type_add(request):
    if request.method == 'POST':
        # On initialise le formulaire avec les données contenues
        form = TypeForm(request.POST)
        # test si le formulaire est valide
        if form.is_valid():
            # On enregistre
            form.save()
        return redirect('index')
    else:
        # si non on initialise un formualire vide
        form = TypeForm()
    return render(request, 'rent/addtype.html', {"form": form})



def tarif_add(request):
    if request.method == 'POST':
        # On initialise le formulaire avec les données contenues
        form = TarifForm(request.POST)
        # test si le formulaire est valide
        if form.is_valid():
            # On enregistre
            form.save()
        return redirect('index')
    else:
        # si non on initialise un formualire vide
        form = TarifForm()
    return render(request, 'rent/addtarif.html', {"form": form})


def taille_add(request):
    if request.method == 'POST':
        # On initialise le formulaire avec les données contenues
        form = TailleForm(request.POST)
        # test si le formulaire est valide
        if form.is_valid():
            # On enregistre
            form.save()
        return redirect('index')
    else:
        # si non on initialise un formualire vide
        form = TailleForm()
    return render(request, 'rent/addtaille.html', {"form": form})
