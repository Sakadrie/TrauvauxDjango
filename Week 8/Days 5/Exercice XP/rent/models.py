from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Customer(models.Model):
    nom = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    phonenumber = PhoneNumberField(blank=True)
    adresse = models.CharField(max_length=200, null=True)
    ville = models.CharField(max_length=200, null=True)
    pays = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nom



class TypeVehicule(models.Model):
    nom = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nom



class TailleVehicule(models.Model):
    nom = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nom



class Vehicule(models.Model):
    type_de_vehicule = models.ForeignKey(TypeVehicule, on_delete=models.CASCADE)
    taille_de_vehicule = models.ForeignKey(TailleVehicule, on_delete=models.CASCADE)
    prix = models.IntegerField()
    date_de_creation = models.DateField()


    def __str__(self):
        return str(self.type_de_vehicule)

class Location(models.Model):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date_de_location = models.DateField()
    date_de_retour = models.DateField()


    def __str__(self):
        return str(self.client)


class Tarif_location(models.Model):
    type_de_vehicule = models.ForeignKey(TypeVehicule, on_delete=models.CASCADE)
    taille_de_vehicule = models.ForeignKey(TailleVehicule, on_delete=models.CASCADE)
    tarif_journalier = models.IntegerField()


    def __str__(self):
        return str(self.type_de_vehicule)

