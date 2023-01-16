from django.contrib import admin
from .models import Reservation
from .models import Customer
# Register your models here.
admin.site.register(Reservation)
admin.site.register(Customer)
