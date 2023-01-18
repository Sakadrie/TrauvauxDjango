from django.urls import path
from . import views

urlpatterns = [
    path('visitor/', views.home, name="home"),
    path('personel/dashboard', views.index, name="index"),
    path('personel/client', views.users, name="users"),
    path('personel/addclient', views.customer_add, name="customer_add"),
    path('personel/reserver', views.reservation, name="reservation"),
    path('personel/addreser', views.rental_add, name="rental_add"),
    path('personel/chambres', views.chambres, name="chambres"),
    path('personel/add_chambre', views.add_chambre, name="add_chambre"),
    path('personel/supprimer', views.delete, name="delete"),
    path('personel/del_sms', views.del_sms, name="del_sms"),
    path('visitor/add_message', views.add_message, name="add_message"),
    path('visitor/message', views.message, name="message"),
   ]