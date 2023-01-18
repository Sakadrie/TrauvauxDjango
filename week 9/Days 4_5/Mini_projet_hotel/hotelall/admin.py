from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Reservation)
admin.site.register(Chambre)
admin.site.register(TypeChambre)
admin.site.register(Avis)