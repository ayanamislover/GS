from django.db import models

# Create your models here.
# models.py
from django.db import models





class QuizSession(models.Model):
    series_id = models.CharField(max_length=255,null=True)
    player = models.CharField(max_length=155)
    score = models.IntegerField(default=0)


