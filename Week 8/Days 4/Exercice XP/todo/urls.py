
from django.urls import path
from . import views
urlpatterns = [
    path('', views.tache, name="tache"),
    path('todo/', views.todo, name="todo"),
    path('categorie/', views.categorie, name="categorie"),

]