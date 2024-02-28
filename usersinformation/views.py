from django.shortcuts import get_object_or_404, render,redirect, reverse
from django.http import HttpResponse
from .models import PlayerProfile
from .forms import PlayerProfileForm, DisplayedAchievementsForm
from django.contrib import messages  # 引入 messages 模块
from django.contrib.auth.decorators import login_required
# Create your views here.

def player_profile_none(request):
    # Render the response using the render function, specifying the template file and context data
    return render(request, 'usersinformation/player_profile_none.html')

# Ensure that the login view stores the user ID in the session
def player_profile2(request,pk):
    # Get the ID of the currently logged in user from session
    # Get the PlayerProfile instance associated with the currently logged in user.
    try:
        player_profile = PlayerProfile.objects.get(pk=pk)
        context = {'player_profile': player_profile}
        return render(request, 'usersinformation/player_profile.html', context)
    except PlayerProfile.DoesNotExist:
        context = {'error': 'Player profile not found.'}
        return render(request, 'usersinformation/error.html', context)


#Test, grab corresponding nicknames, display user interface
def detailnickname(request, nickname):

    player_information = get_object_or_404(PlayerProfile, nickname=nickname)
    # Transmit the information to html model
    return render(request, "usersinformation/player_profile.html", {"player_information": player_information})


def player_profile(request, nickname):
    try:
        # Getting a PlayerProfile instance by nickname
        player_information = get_object_or_404(PlayerProfile, nickname=nickname)
        # Getting all achievements information
        all_achievements = player_information.achievements.all()

        # Get the number of unlocked achievements by calling the method directly from the instance
        unlocked_achievement_count = player_information.unlocked_achievement_count()
        # Get the achievements that the user has chosen to display, if not, then the first three of all achievements will be displayed by default
        displayed_achievements = player_information.displayed_achievements.all()[:3] if player_information.displayed_achievements.exists() else all_achievements[:3]
        # Passing the acquired user information and achievements to the template
        return render(request, "usersinformation/player_profile.html", {
            "player_information": player_information,
            "all_achievements": all_achievements,
            "displayed_achievements": displayed_achievements,
            "unlocked_achievement_count":unlocked_achievement_count,
            #"user_email": user_
        })
    except PlayerProfile.DoesNotExist:
        # If the associated PlayerProfile is not found, you can render an error page or do something else with it
        context = {'error': 'Player profile not found.'}
        return render(request, 'usersinformation/error.html', context)


#Defining the Edit Page View
def edit_player_profile(request, nickname):
    player_profile = get_object_or_404(PlayerProfile, nickname=nickname)
    # If the request is a POST, process the form data
    if request.method == 'POST':
        profile_form = PlayerProfileForm(request.POST, request.FILES, instance=player_profile)
        achievements_form = DisplayedAchievementsForm(request.POST, instance=player_profile, user_nickname=nickname)
        # Check if both forms are valid
        if profile_form.is_valid() and achievements_form.is_valid():
            profile_form.save()
            #Save the information
            achievements_form.save()
            messages.success(request, 'Profile and achievements updated successfully!')
            # return redirect('player_profile', nickname=player_profile.nickname)
            return redirect(reverse('usersinformation:player_profile', kwargs={"nickname":player_profile.nickname}))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        # If not a POST request, initialise the form
        profile_form = PlayerProfileForm(instance=player_profile)
        achievements_form = DisplayedAchievementsForm(instance=player_profile, user_nickname=nickname)

    # Pass two forms to the template
    return render(request, 'usersinformation/edit_player_profile2.html', {
        'profile_form': profile_form,
        'achievements_form': achievements_form
    })
