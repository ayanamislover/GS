from imaplib import _Authenticator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from aM.models import Activity
from django.core.exceptions import ObjectDoesNotExist
from activityboard.views import generate_qrcode
from gamekeeper.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from pictures.models import Photo
from usersinformation.models import PlayerProfile
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)  # Make sure user is passed in here
                    return redirect('gamekeeper')  # redirect'gamekeeper' URL
                else:
                    return render(request, 'gamekeeperlogin.html', {'form': form, 'error': 'Account unavailable'})
            else:
                return render(request, 'gamekeeperlogin.html', {'form': form, 'error': 'The user name or password is incorrect'})
    else:
        form = LoginForm()
    return render(request, 'gamekeeperlogin.html', {'form': form})

@login_required
def gamekeeper(request):
    return render(request, 'gamekeeper.html')

@csrf_exempt
@login_required
def gamekeeper_qrcode(request):
    if request.method == 'POST':
        series_id = request.POST.get('series_id')
        return redirect('qrcode', series_id=series_id)
    else:
        # If it is not a POST request, the form or error message is displayed
        return render(request, 'get_qrcode.html')


@csrf_exempt
@login_required
def change_status(request):
    message = ''  # Used to display information to the user
    if request.method == 'POST':
        title = request.POST.get('title')
        status = request.POST.get('status')
        try:
            activity = Activity.objects.get(title=title)
            activity.status = status
            activity.save()
            message = 'Activity status updated successfully!'
        except Activity.DoesNotExist:
            message = 'Activity not found.'
        except Exception as e:
            message = str(e)
    return render(request, 'change_statue.html', {'message': message})


@csrf_exempt
@login_required
def review_photos(request):
    if request.method == 'POST':
        action = request.POST.get('action', '')
        photo_id = action.split('_')[-1]

        if 'approve' in action:
            photo = Photo.objects.get(id=photo_id)
            player = PlayerProfile.objects.get(nickname=photo.nickname)
            player.score += 1  # add score
            player.save()
        
        # Regardless of bonus points or not, delete the picture
        Photo.objects.get(id=photo_id).delete()

        return redirect('review_photos')  # Reload the page to update the list of images to be reviewed

    photos = Photo.objects.all()  # Get all images pending review
    return render(request, 'review_photos.html', {'photos': photos})
