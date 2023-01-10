from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    phone_number = models.PhoneNumberField()
    address = models.CharField(max_length=200, null=True)
