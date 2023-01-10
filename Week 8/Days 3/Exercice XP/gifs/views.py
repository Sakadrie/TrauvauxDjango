from django.shortcuts import render, redirect
from .models import Gifs
from .models import Categorie
from .forms import GifForm
from .forms import CategoryForm
# Create your views here.

def gif(request):
    gifss = Gifs.objects.all()
    return render(request, "index.html", {"gifss": gifss})

def giffs(request, id):
    giff = Gifs.objects.get(id=id)
    return render(request, "Gif.html", {"giff": giff})


def categorie(request, id):
    category = Categorie.objects.get(id=id)
    return render(request, "Categori.html", {"category": category})

def categories(request):
    categoris = Categorie.objects.all()
    return render(request, "Categories.html", {"categoris": categoris})


def AjoutGif(request):
    gifss = Gifs.objects.all()
    if request.method == 'POST':
        form = GifForm(request.POST)
        if form.is_valid():
            form.save()
            form = GifForm()

    else:
        form = GifForm()
    context = {
        "gifss": gifss,
        "form": form,
    }

    return render(request, "AjoutGif.html", context)


def AjoutCate(request, nom):
    categoris = Categorie.objects.get(nom=nom)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            form = CategoryForm()

    else:
        form = CategoryForm()
    context = {
        "categoris": categoris,
        "form": form,
    }

    return render(request, "AjoutCategori.html", context)

