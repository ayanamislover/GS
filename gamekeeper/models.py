from django.db import models

# Create your models here.
class gamekeeper(models.Model):
    keepername = models.CharField(max_length=255, blank=True)
