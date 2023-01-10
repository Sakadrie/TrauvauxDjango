from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('rent/rental/', views.rental, name="rental"),
    path('rent/rental/<int:id>', views.rentals, name="rentals"),
    path('rent/rental/add', views.rental_add, name="rental_add"),
    path('rent/customer/<int:id>', views.customers, name="customers"),
    path('rent/customer/', views.customer, name="customer"),
    path('rent/customer/', views.generate_faker, name="generate_faker"),
    path('rent/customer/add', views.customer_add, name="customer_add"),
    path('rent/vehicule/', views.vehicule, name="vehicule"),
    path('rent/vehicule/<int:id>', views.vehicules, name="vehicules"),
    path('rent/vehicule/add', views.vehicule_add, name="vehicule_add")
]
