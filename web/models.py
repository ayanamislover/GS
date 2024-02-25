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

admin.site.register(User, UserAdmin)


