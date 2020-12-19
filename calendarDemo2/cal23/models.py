from django.db import models
from datetime import datetime

# Create your models here.


class Event(models.Model):
    name = models.CharField('Event Name', max_length=50, default=False)
    event_date = models.DateTimeField('Event Date', default='null')
    venue = models.CharField(max_length=150, default="null")
    manager = models.CharField(max_length=60, default='m')
    description = models.TextField(blank=True, default="null")
