from django.db import models

class Person(models.Model):
    person_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
