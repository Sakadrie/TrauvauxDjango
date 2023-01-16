from django.urls import path
from . import views

urlpatterns = [
    path('personel/dashboard', views.index, name="index"),
    path('personel/reservation', views.reservation, name="reservation"),
    path('personel/addreser', views.reservation_add, name="reservation_add"),
    path('personel/addclient', views.add_client, name="add_client"),
    path('personel/upadreser/<int:id>', views.update_reser, name="update_reser"),
    path('personel/delreser/<int:id>', views.delete_reser, name="delete_reser"),
    path('personel/read/<int:id>', views.read_message, name="read_message"),
    path('personel/delsms/<int:id>', views.delete_comment, name="delete_comment"),
   ]
