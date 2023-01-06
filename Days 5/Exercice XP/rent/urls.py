from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('rent/rental/', views.rental, name="rental"),
    path('rent/rental/<int:id>', views.rental, name="rental"),
    path('rent/rental/add', views.rental, name="rental"),
    path('rent/customer/<int:id>', views.customer, name="customer"),
    path('rent/customer/', views.customer, name="customer"),
    path('rent/customer/add', views.customer, name="customer"),
    path('rent/vehicule/', views.vehicule, name="vehicule"),
    path('rent/vehicule/<int:id>', views.vehicule, name="vehicule"),
    path('rent/vehicule/add', views.vehicule, name="vehicule")
]
