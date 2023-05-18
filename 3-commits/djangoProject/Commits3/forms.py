from django import forms
from django.forms import ModelForm

from .models import *


class AdForm(ModelForm):
    class Meta:
        model = Ad
        exclude = ('publicationDate', 'expirationDate')
        labels = {'name': 'Tytuł ogłoszenia', 'description': 'Opis'}
