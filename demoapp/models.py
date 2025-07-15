from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length = 100)
    cuisine = models.CharField(max_length = 100)
    price = models.IntegerField()   # don't have to pass anything to it

    def __str__(self):
        return f"{self.name} : {self.cuisine}"

class Customer(models.Model):
    name = models.CharField(max_length = 255)
    reservation_day = models.CharField(max_length = 20, default = 'Monday')
    seats = models.IntegerField(default = 2)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name = models.CharField(max_length = 255)
    customer = models.ForeignKey(
        Customer, 
        on_delete = models.CASCADE,
        related_name = 'Vehicle'
    )