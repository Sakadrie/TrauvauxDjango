from django.contrib import admin
from .models import Reservation
from .models import Message
from .models import Hotel
# Register your models here.

admin.site.register(Reservation)
admin.site.register(Message)
admin.site.register(Hotel)