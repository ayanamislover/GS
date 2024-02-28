from __future__ import unicode_literals
# 导入Django的模型模块
from django.db import models
from django.db import models, transaction
from django.contrib import admin
from usersinformation.models import PlayerProfile


# 定义User模型类
from django.contrib.auth.hashers import make_password

class User(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    # OneToOneField关联到PlayerProfile
    player_profile = models.OneToOneField(PlayerProfile, on_delete=models.CASCADE, null=True, related_name='user')

    def save(self, *args, **kwargs):
        # 首先保存User对象
        super(User, self).save(*args, **kwargs)
        # 然后获取或创建PlayerProfile实例
        player_profile, created = PlayerProfile.objects.get_or_create(user=self)
        # 如果是新创建的PlayerProfile，设置其额外的字段
        if created:
            player_profile.nickname = self.username
            player_profile.email = self.email  # 假设PlayerProfile模型有email字段
            player_profile.save()


    #def set_password(self, raw_password):
    #    self.password = make_password(raw_password)
    #    self.save()



class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(User, UserAdmin)


