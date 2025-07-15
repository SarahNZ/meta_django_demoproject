from unicodedata import name
from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length = 100)
    cuisine = models.CharField(max_length = 100)
    price = models.IntegerField()   # don't have to pass anything to it

    def __str__(self):
        return f"{self.name} : {self.cuisine}"