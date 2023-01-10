from django.shortcuts import render
from .models import Animal
from .models import Famille
from .models import Animaux
# Create your views here.

def animal(request, id):
    animals = Animal.objects.get(id=id)
    context = {"animals": animals}
    return render(request, "animal.html", context )

def famille(request, id):
    familles = Animal.objects.filter(family=id)
    context = {"famille": familles}
    return render(request, "family.html", context )

def animaux(request):
    listanimal = Animaux.objects.all()
    context = {"animals": listanimal}
    return render(request, "index.html", context)
