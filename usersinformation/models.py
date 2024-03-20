from django.db import models
#from django.contrib.auth.models import User


from django.conf import settings

from achievement.models import Achievement
from answerquestion.models import Series
#from web.models import User

# Create your models here.
class PlayerProfile(models.Model):

    #Avatr
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    # Nickname
    nickname = models.CharField(max_length=255, blank=True)

    #Email
    email = models.EmailField(blank=True)
    #Score
    score = models.IntegerField(default=0)

    # User's achievement counts
    achievement_count = models.IntegerField(default=0)

    #User's achievement
    achievements = models.ManyToManyField(Achievement, blank=True, related_name='user')  # 添加多对多关系

    # Displayed selected achievements
    displayed_achievements = models.ManyToManyField(Achievement, related_name='displayed_by_users', blank=True)

    # Bio
    bio = models.TextField(blank=True)

    # Login_days
    login_days = models.IntegerField(default=0)

    carbon = models.IntegerField(default=0)

    #lcy
    last_game_start = models.DateTimeField(null=True, blank=True)
    verified_locations_count = models.IntegerField(default=0)

    #Completed quize status
    completed_series = models.ManyToManyField(Series, related_name='completed_by', blank=True)

    def unlock_achievements(self):
        # Get all unlocked achievements with unlock points lower or equal to the user's current points
        unlockable_achievements = Achievement.objects.filter(unlock_score__lte=self.score)
        for achievement in unlockable_achievements:
            self.achievements.add(achievement)

    # New method to dynamically count the number of achievements a user has unlocked
    def unlocked_achievement_count(self):
        return Achievement.objects.filter(unlock_score__lte=self.score).count()

    def __str__(self):
        return f"{self.avatar} {self.nickname} {self.email} {self.achievement_count} {self.bio} {self.login_days}"


# the record for achievement
class AchievementAndUser(models.Model):
    user = models.ForeignKey(PlayerProfile, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.achievement} {self.created_at}"
