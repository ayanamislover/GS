from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_checked_in = models.BooleanField(default=False)
    def __str__(self):
        return self.name
