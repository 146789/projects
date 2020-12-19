from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    Image = models.FilePathField(path="\img")
