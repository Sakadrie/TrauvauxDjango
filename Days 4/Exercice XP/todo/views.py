from django.shortcuts import render, redirect
from .models import Todo
from .models import Categorie
from .forms import TacheForm

# Create your views here.

def todo(request):
    todo = Todo.objects.all()
    return render(request, "Display.html", {"todo": todo})

def tache(request):
    if request.method == "GET":
        form = TacheForm()
        return render(request, 'Ajouttodo.html', {'form': form})

    if request.method == "POST":

        form = TacheForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('todo')

def categorie(request):
    category = Categorie.objects.all()
    context = {"categorie": category}
    return render(request, "Display.html", context)