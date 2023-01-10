from django import forms
from . import models
from .models import Gifs
from .models import Categorie


class GifForm(forms.ModelForm):
     class Meta:
        models = Gifs
        fields = ('title', 'url', 'uploader_name', 'categories = forms.ModelMultipleChoiceField(queryset=None)')



class CategoryForm(forms.ModelForm):
    class Meta:
        models = Categorie
        fields = ('nom = models.CharField(max_length=100, null=True)')

