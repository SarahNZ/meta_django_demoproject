from django.db import models

# Implementation using ModelForm class

class Input(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    time_log = models.TimeField(help_text = "Enter the exact time")

# class Person(models.Model):
#     person_name = models.CharField(max_length=20)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)
