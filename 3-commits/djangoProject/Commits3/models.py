from django.db import models
from datetime import date, datetime, timedelta


# Create your models here.
class Ad(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=2000, null=False, blank=False)
    cost = models.FloatField(verbose_name='Cena', null=False, blank=False)
    publicationDate = models.DateTimeField(default=datetime.now(), blank=True)
    expirationDate = models.DateTimeField(default=(datetime.now() + timedelta(days=14)), blank=True)

    def __str__(self):
        return 'ID: ' + str(self.pk) + \
               'Nazwa ogłoszenia: ' + str(self.name) + \
               ' Cena: ' + str(self.cost) + \
               ' Data publikacji: ' + str(self.publicationDate + timedelta(hours=2)) + \
               ' Data przedawnienia: ' + str(self.expirationDate + timedelta(hours=2))
