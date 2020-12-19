from django.db import models

# Create your models here.


class student(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=40)
    testscore = models.FloatField()
