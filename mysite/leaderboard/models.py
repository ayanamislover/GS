from django.db import models

# Create your models here.

class leaderboard(models.Model):
    username = models.CharField(max_length=150)
    score = models.IntegerField(default=0)  # score
    achievements = models.IntegerField(default=0)  # number of achievements
    login_days = models.IntegerField(default=0)  # days of user login
    carbon_footprint = models.FloatField(default=0.0)  # 碳足迹

    def __str__(self):
        return self.username #force it to express like string
