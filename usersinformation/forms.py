# forms.py
from django import forms
from django.forms import ModelForm
from .models import PlayerProfile
from achievement.models import Achievement

#创建PlayerProfileForm表单实列，从ModelForm类引用，基于已有模型创建表单字段
class PlayerProfileForm(forms.ModelForm):
    class Meta:
        model = PlayerProfile
        fields = ['avatar','nickname', 'email', 'bio']

#创建一个表单来允许用户选择他们要展示的成就。这个表单可以是一个ModelForm，它将包含displayed_achievements字段。
#class DisplayedAchievementsForm(forms.ModelForm):
 #   class Meta:
  #      model = PlayerProfile
   #     fields = ['displayed_achievements']
    #    widgets = {
     #       'displayed_achievements': forms.CheckboxSelectMultiple()
      #  }



class DisplayedAchievementsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user_nickname = kwargs.pop('user_nickname', None)  # 从kwargs中获取user_pk，并在之后删除这个键值对
        super(DisplayedAchievementsForm, self).__init__(*args, **kwargs)
        if user_nickname:
            player_profile = PlayerProfile.objects.get(nickname=user_nickname)
            # 过滤成就：只显示玩家已经解锁的成就
            self.fields['displayed_achievements'].queryset = Achievement.objects.filter(
                unlock_score__lte=player_profile.score)

    class Meta:
        model = PlayerProfile
        fields = ['displayed_achievements']
        widgets = {
            'displayed_achievements': forms.CheckboxSelectMultiple()
        }