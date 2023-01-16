from django.shortcuts import render
from .models import Hotel
from .models import Reservation
from .forms import ReserverForm
from .forms import MessageForm
from faker import Faker
from django.shortcuts import render, redirect
from .models import Message
# Create your views here.
def index1(request):
   return render(request, 'visitor/index.html')

def hotelinfo(request):
    info = Hotel.objects.all()
    return render(request, 'visitor/index.html', {"info": info})



def reservation_add(request):
    if request.method == 'POST':
        # On initialise le formulaire avec les données contenues
        form = ReserverForm(request.POST)
        # test si le formulaire est valide
        if form.is_valid():
            # On enregistre
            form.save()
    else:
        # si non on initialise un formualire vide
        form = ReserverForm()
    return render(request, 'visitor/index.html', {"form": form})

def add_message(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        comment = request.POST.get('comment')
        Message.objects.create(nom=nom, email=email, phone_number=phone_number, comment=comment)
        return redirect('success_view')
    else:
        return render(request, 'visitor/index.html')


