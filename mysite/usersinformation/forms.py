# forms.py
from django import forms
from django.forms import ModelForm
from .models import PlayerProfile

#创建PlayerProfileForm表单实列，从ModelForm类引用，基于已有模型创建表单字段
class PlayerProfileForm(forms.ModelForm):
    class Meta:
        model = PlayerProfile
        fields = ['avatar','nickname', 'email', 'bio']

#创建一个表单来允许用户选择他们要展示的成就。这个表单可以是一个ModelForm，它将包含displayed_achievements字段。
class DisplayedAchievementsForm(forms.ModelForm):
    class Meta:
        model = PlayerProfile
        fields = ['displayed_achievements']
        widgets = {
            'displayed_achievements': forms.CheckboxSelectMultiple()
        }
