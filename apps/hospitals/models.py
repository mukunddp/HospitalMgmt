from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SavePatient(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    weight = models.CharField(max_length=3)
    gender = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    serv = models.ForeignKey(User, on_delete=models.CASCADE)
    services = models.CharField(max_length=40)


class Total(models.Model):
    count = models.BigIntegerField


class Prescription(models.Model):
    pt = models.ForeignKey('hospitals.SavePatient', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    tablets = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
