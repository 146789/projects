from django.db import models

# Create your models here.


class Hotel_image(models.Model):
    name = models.CharField(max_length=50)
    Hotel_images = models.ImageField(upload_to='images/')
