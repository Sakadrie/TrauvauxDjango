from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    ADMIN = 'ADMIN'
    CUSTOMER = 'CUSTOMER'
    ROLE = [(ADMIN, 'Admin'), (CUSTOMER, 'Customer')]

    profile_photo = models.ImageField(upload_to='upload_image/', verbose_name="Photo de profil", null=True)
    role = models.CharField(max_length=50, choices=ROLE, verbose_name='Role')

    def profile_photoURL(self):
        try:
            url =self.profile_photo.url
        except:
            url= ''
        return url