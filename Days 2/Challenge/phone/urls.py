from django.urls import path
from . import views
urlpatterns = [
    path('', views.person_number, name="person_number"),
    path('person_name/', views.person_name, name="person_name"),
]