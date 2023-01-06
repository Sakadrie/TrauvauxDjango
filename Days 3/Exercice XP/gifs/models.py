from django.db import models

# Create your models here.
class Gifs(models.Model):
    title = models.CharField(max_length=200, null=True)
    url = models.URLField()
    uploader_name = models.CharField(max_length=200, null=True)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Categorie(models.Model):
    nom = models.CharField(max_length=100, null=True)
    gifs = models.ManyToManyField(Gifs, related_name='categories', blank=True)

    def __str__(self):
        return self.nom