from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Hotel(models.Model):
    nom = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    libelle = models.TextField()
    vacancians = models.TextField()
    def __str__(self):
        return self.nom

    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Reservation(models.Model):
    date_ari = models.DateField()
    date_sorti = models.DateField()
    number_person = models.IntegerField()
    number_chambre = models.IntegerField()

    def __str__(self):
        return str(self.date_ari)

class Message(models.Model):
    nom = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    comment = models.TextField(blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    def __str__(self):
        return self.nom