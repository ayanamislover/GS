# forms.py
from django import forms
from django.forms import ModelForm
from .models import PlayerProfile

#创建PlayerProfileForm表单实列，从ModelForm类引用，基于已有模型创建表单字段
class PlayerProfileForm(forms.ModelForm):
    class Meta:
        model = PlayerProfile
        fields = ['nickname', 'email', 'bio']
