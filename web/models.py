from __future__ import unicode_literals
# 导入Django的模型模块
from django.db import models
from django.contrib import admin


# 定义User模型类
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')

    # 定义对象的字符串表示方法，返回用户名
    def __str__(self):
        return self.username


