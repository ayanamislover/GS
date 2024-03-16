from imaplib import _Authenticator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from aM.models import Activity
from django.core.exceptions import ObjectDoesNotExist
from activityboard.views import generate_qrcode
from gamekeeper.forms import LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)  # 确保这里传入了user
                    return redirect('gamekeeper')  # 假设你有一个名为'gamekeeper'的URL
                else:
                    return render(request, 'gamekeeperlogin.html', {'form': form, 'error': '账户不可用'})
            else:
                return render(request, 'gamekeeperlogin.html', {'form': form, 'error': '用户名或密码错误'})
    else:
        form = LoginForm()
    return render(request, 'gamekeeperlogin.html', {'form': form})

def gamekeeper(request):
    return render(request, 'gamekeeper.html')

def gamekeeper_qrcode(request):
    if request.method == 'POST':
        series_id = request.POST.get('series_id')
        return redirect('qrcode', series_id=series_id)
    else:
        # If it is not a POST request, the form or error message is displayed
        return render(request, 'get_qrcode.html')

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