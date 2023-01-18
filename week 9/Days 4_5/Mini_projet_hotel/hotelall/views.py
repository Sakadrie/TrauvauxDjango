from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReserverForm
from .models import Message
from django.contrib import messages
from .forms import CustomerForm

# Create your views here.
def index(request):
    return render(request, 'personel/dashboard.html')

def add_client(request):
    if request.method == 'POST':
        # On initialise le formulaire avec les données contenues
        form = CustomerForm(request.POST)
        # test si le formulaire est valide
        if form.is_valid():
            # On enregistre
            form.save()
    else:
        # si non on initialise un formualire vide
        form = CustomerForm()
    return render(request, 'personel/addclient.html', {"form": form})

def reservation(request):
    reservation = Reservation.objects.all()
    return render(request, 'personel/reserver.html', {"reservation": reservation})

def reservation_add(request):
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

def update_reser(request, id):
    reservation = Reservation.objects.get(id=id)
    if request.method == 'POST':
        form = ReserverForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"successfully {reservation.nom} was edited !")
            return redirect('reservation')
        else:
            form = ReserverForm(instance=reservation)
        return render(request, 'personel/update.html', {'form': form})



def delete_reser(request, id):
    reservat = Reservation.objects.get(id=id)
    if request.method == 'POST':
        reservat.delete()
        return redirect("reservation")
    return render(request, "personel/delete.html", {"reservat": reservat})

def read_message(request, id):
    messe = Message.objects.get(id=id)
    mes = messe.comment
    return render(request, "personel/read.html", {"mes": mes})

def delete_comment(request, id):
    mess_del = Message.objects.get(id=id)
    mess = mess_del.comment
    if request.method == 'POST':
        mess_del.delete()
        return redirect("read")
    return render(request, "personel/delete.html", {"mess": mess})

