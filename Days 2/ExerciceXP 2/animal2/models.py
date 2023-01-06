from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=200, null=True)
    legs = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    speed = models.IntegerField()
    family = models.IntegerField()

    def __str__(self):
        return self.name

class Famille(models.Model):
    nom = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nom


class Animaux(models.Model):
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name



