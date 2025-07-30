from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    contact = models.CharField(max_length = 15)
    class Meta:
        db_table = "Employee"

class Menu(models.Model):
    name = models.CharField(max_length = 100)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

class Input(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    time_log = models.TimeField(help_text = "Enter the exact time")

class Person(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    # person_name = models.CharField(max_length=20)
    # email = models.EmailField()
    # phone = models.CharField(max_length=20)

class Reservation(models.Model):
    first_name = models.CharField(max_length = 100, blank = True)
    last_name = models.CharField(max_length = 100, null = True, blank = True, default = "Unknown")
    booking_time = models.DateTimeField(auto_now = True)
    # contact = models.CharField('Phone number', max_length = 100)
    # time = models.TimeField()
    # count = models.IntegerField()
    # notes = models.CharField(max_length = 300, blank = True)

    def __str__(self):
        return self.name