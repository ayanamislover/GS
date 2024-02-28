from django.db import models
from django.contrib.auth.models import User


class Achievement(models.Model):
    name = models.CharField(max_length=255, unique=True)  # 成就名称
    description = models.TextField()  # 成就描述
    icon = models.ImageField(upload_to='images/', null=True, blank=True)  # 成就图标
    unlock_score = models.IntegerField(default=0)  # 解锁成就所需的积分
    def __str__(self):
        return self.name

#这个实例基本也没啥用
# UserAchievement模型使用ForeignKey字段与User和Achievement模型建立了关联
class UserAchievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    #unlocked字段是一个布尔字段，用于标记成就是否已经被用户解锁。
    unlocked = models.BooleanField(default=False)
    #unlock_date字段是一个日期时间字段，用于记录用户解锁该成就的日期和时间。
    unlock_date = models.DateTimeField(null=True, blank=True)
    #unique_together选项确保每个用户和成就的组合是唯一的，这意味着同一个用户不能解锁同一个成就多次。
    class Meta:
        unique_together = (('user', 'achievement'),)

    def __str__(self):
        return f"{self.user.username} - {self.achievement.name}"

