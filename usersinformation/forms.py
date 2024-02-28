# forms.py
from django import forms
from django.forms import ModelForm
from .models import PlayerProfile
from achievement.models import Achievement

#Create PlayerProfileForm form real columns, referenced from ModelForm class, creating form fields based on existing model
class PlayerProfileForm(forms.ModelForm):
    class Meta:
        model = PlayerProfile
        fields = ['avatar','nickname', 'email', 'bio']

#Create a form to display user's achievement
class DisplayedAchievementsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user_nickname = kwargs.pop('user_nickname', None)  #\
        super(DisplayedAchievementsForm, self).__init__(*args, **kwargs)
        if user_nickname:
            player_profile = PlayerProfile.objects.get(nickname=user_nickname)
            # Filter Achievements: Show only achievements that the player has unlocked
            self.fields['displayed_achievements'].queryset = Achievement.objects.filter(
                unlock_score__lte=player_profile.score)
    class Meta:
        model = PlayerProfile
        fields = ['displayed_achievements']
        widgets = {
            'displayed_achievements': forms.CheckboxSelectMultiple()
        }