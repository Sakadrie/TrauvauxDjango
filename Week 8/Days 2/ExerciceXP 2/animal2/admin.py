from django.contrib import admin
from .models import Animal
from .models import Famille
from .models import Animaux
# Register your models here.
admin.site.register(Animal)
admin.site.register(Famille)
admin.site.register(Animaux)