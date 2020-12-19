from django.db import models

# Create your models here.


class Register(models.Model):
    collageaname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    roll = models.CharField(max_length=15)
    branch = models.CharField(max_length=60)
    year = models.IntegerField()
