from django.db import models

# Create your models here.
# models.py
from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)  # location name
    latitude = models.FloatField()  # latitude
    longitude = models.FloatField()  # longitude
    radius = models.IntegerField()  # radius(m)

    def __str__(self):
        return self.name


class QuizSession(models.Model):
    series_id = models.CharField(max_length=255,null=True)
    player = models.CharField(max_length=155)
    score = models.IntegerField(default=0)


