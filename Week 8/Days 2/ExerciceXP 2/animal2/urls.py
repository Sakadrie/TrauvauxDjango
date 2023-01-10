from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.animaux, name="index"),
    path('animal/<int:id>', views.animal, name="animal"),
    path('famille/<int:id>', views.famille, name="famille"),

]