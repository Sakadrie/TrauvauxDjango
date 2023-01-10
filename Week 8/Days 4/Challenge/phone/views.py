from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import Person
# Create your views here.

def person_number(request, phone_number):
    phone_number = Person.objects.get(phone_number=phone_number)
    return render(request, 'phone_number.html', {'phone_number': phone_number })


def person_name(request, name):
    person_nom = Person.objects.get(name=name)
    return render(request, 'person_name.html', {'person_nom': person_nom})
