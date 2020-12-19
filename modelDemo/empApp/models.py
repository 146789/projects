from django.db import models

# Create your models here.


class Employee(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    salary = models.FloatField()
    email = models.CharField(max_length=40)


class Programmer(models.Model):
    name = models.CharField(max_length=40)
    salary = models.IntegerField()


class Project(models.Model):
    name = models.CharField(max_length=40)
    programmers = models.ManyToManyField(Programmer)


class Customer(models.Model):
    name = models.CharField(max_length=30)


class PhoneNumber(models.Model):
    Type = models.CharField(max_length=15)
    Number = model.CharField(max_length=16)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
