from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Customer(models.Model):
    nom = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    phonenumber = PhoneNumberField(blank=True)
    address = models.CharField(max_length=200, null=True)
    ville = models.CharField(max_length=200, null=True)
    pays = models.CharField(max_length=200, null=True)
    def __str__(self):
        return f'{self.nom}  {self.prenom}'

class Avis(models.Model):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    avis = models.CharField(max_length=70, null=True)

    def __str__(self):
        return str(self.client)
class TypeChambre(models.Model):
    typecharmbre = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.typecharmbre

class Chambre(models.Model):
    model = models.ForeignKey(TypeChambre, on_delete=models.CASCADE)
    cout = models.IntegerField()
    taille = models.IntegerField()
    photo = models.ImageField(verbose_name='photo de chambre', default='img_chambre/default.jpg',
                              upload_to='img_chambre')
    def photoUrl(self):
        try:
            url = self.photo.url
        except:
            url = "img_chambre/default.jpg"
        return url

    def __str__(self):
        return str(self.model)

class Reservation(models.Model):
    date_ari = models.DateField()
    date_sorti = models.DateField()
    number_person = models.IntegerField()
    number_chambre = models.IntegerField()
    cout = models.IntegerField()
    statu = models.BooleanField()
    typechambre = models.ForeignKey(TypeChambre, on_delete=models.CASCADE)
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.client)





