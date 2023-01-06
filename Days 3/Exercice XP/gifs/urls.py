from django.urls import path
from . import views
urlpatterns = [
    path('', views.gif, name="gif"),
    path('giffs/<int:id>', views.giffs, name="giffs"),
    path('categories/', views.categories, name="categories"),
    path('categorie/<int:id>', views.categorie, name="categorie"),
    path('AjoutGif/', views.AjoutGif, name="ajoutGif"),
    path('AjoutCate/', views.AjoutCate, name="ajoutCate")
]