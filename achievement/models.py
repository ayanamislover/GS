from django.db import models
from django.contrib.auth.models import User
class Achievement(models.Model):
    #Achievement name
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    #Image
    icon = models.ImageField(upload_to='achievement/images/', null=True, blank=True)
    #Unlock the achievement
    unlock_score = models.IntegerField(default=0)
    def __str__(self):
        return self.name

#Not use
class UserAchievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)

    unlocked = models.BooleanField(default=False)

    unlock_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = (('user', 'achievement'),)

    def __str__(self):
        return f"{self.user.username} - {self.achievement.name}"