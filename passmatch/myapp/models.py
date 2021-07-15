from django import forms
from django.db import models

class Person(models.Model):
    namee = models.CharField(max_length=90)
    name1 = models.CharField(max_length=90, default='')



# Create your models here.
