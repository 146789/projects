from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    roll = models.CharField(max_length=20)
    phno = models.IntegerField()

class Faculty(models.Model):
    f_name = models.CharField(max_length = 40)
    f_age = models.IntegerField()
    f_empid = models.IntegerField()
    f_phno = models.IntegerField()
    f_email = models.EmailField()