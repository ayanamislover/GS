from django.db import models
from django.contrib.auth.models import User


from django.conf import settings

from achievement.models import Achievement
from answerquestion.models import Series


# Create your models here.
class PlayerProfile(models.Model):
    #关联到Django内置User模型，实现每一个用户注册一个用户信息对象
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    #头像
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    # 用户昵称
    nickname = models.CharField(max_length=255, blank=True)

    # 用户邮箱
    email = models.EmailField(unique=True)

    score = models.IntegerField(default=0)  # 用户积分

    # 用户成就数量
    achievement_count = models.IntegerField(default=0)
    #用户的成就
    achievements = models.ManyToManyField(Achievement, blank=True, related_name='user')  # 添加多对多关系

    # 可选：用于选择展示的成就
    displayed_achievements = models.ManyToManyField(Achievement, related_name='displayed_by_users', blank=True)

    # 用户个性签名
    bio = models.TextField(blank=True)

    # 用户登录天数
    login_days = models.IntegerField(default=0)

    #完成答题系列信息
    completed_series = models.ManyToManyField(Series, related_name='completed_by', blank=True)

    def unlock_achievements(self):
        # 获取所有未解锁的成就，其解锁积分低于或等于用户当前积分
        unlockable_achievements = Achievement.objects.filter(unlock_score__lte=self.score)
        for achievement in unlockable_achievements:
            self.achievements.add(achievement)

    #加入str方法，每次使用PlayerProfile对象时，返回有意义字符串。返回人类可读模型表示
    def __str__(self):
        return f"{self.avatar} {self.nickname} {self.email} {self.achievement_count} {self.bio} {self.login_days}"
