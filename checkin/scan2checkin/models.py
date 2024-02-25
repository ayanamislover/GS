from django.db import models

class Activity(models.Model):
    code = models.CharField(max_length=100, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()