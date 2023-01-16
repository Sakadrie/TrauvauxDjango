from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Customer(models.Model):
    nom = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    phonenumber = PhoneNumberField(blank=True)
    adresse = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.nom}__{self.prenom}__{self.phonenumber}__{self.adresse}'


class Reservation(models.Model):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_res= models.DateField()
    date_sorti = models.DateField()
    number_person = models.IntegerField()
    number_chambre = models.IntegerField()


    def __str__(self):
        return str(self.client)