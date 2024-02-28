from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Gift(models.Model):
    name = models.CharField(max_length=100)
    points = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Create your models here.
