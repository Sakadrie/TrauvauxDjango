from django.contrib import admin
from .models import Customer
from .models import Vehicule
from .models import TypeVehicule
from .models import TailleVehicule
from .models import Tarif_location
from .models import Location
# Register your models here.
admin.site.register(Customer)
admin.site.register(Location)
admin.site.register(Vehicule)
admin.site.register(TypeVehicule)
admin.site.register(TailleVehicule)
admin.site.register(Tarif_location)