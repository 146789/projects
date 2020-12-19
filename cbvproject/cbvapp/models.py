from django.db import models

# Create your models here.


class Student(models.Model):
    firstName = models.CharField(max_length=80)

    lastName = models.CharField(max_length=80)
    Tscore = models.FloatField()
