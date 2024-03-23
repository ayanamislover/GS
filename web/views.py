from django.http import HttpResponse
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from decorate import login_requiredforuser
from django.urls import reverse
from django.views.decorators.cache import never_cache

# Make sure you have imported the User and PlayerProfile models from your model files
from .models import User
from usersinformation.models import PlayerProfile
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login  # Import authenticate and login functions
from django.views.decorators.csrf import csrf_exempt
# Define user forms
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')



# Register view

from django.contrib.auth.hashers import make_password

# User regist
@csrf_exempt
def regist(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)

        if userform.is_valid():
            print("Begin regist:")
            # Get data from form
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']

            # Check uniqueness
            if User.objects.filter(username=username).exists():
                # If already exist, send a error message
                userform.add_error('username', 'The username is already taken. Please choose another one.')
                return render(request, 'regist.html', {'userform': userform})

            # hash password
            hashed_password = make_password(password)

            
            pp = PlayerProfile.objects.create(email=email, nickname=username)
            print("regist successfully：", pp)
            user = User.objects.create(username=username, password=hashed_password, email=email, player_profile=pp)
            print("regist successfully：", user)

            # return to login page
            return redirect(reverse('login'))
        else:
            print("form error")
            
            return render(request, 'regist.html', {'userform': userform})
    else:
        # For Get request or other not Post, show a empty form
        userform = UserForm()
        return render(request, 'regist.html', {'userform': userform})



# Login view
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
# from.forms import UserForm # Make sure you have imported UserForm correctly


# user login
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                request.session['is_logged_in'] = True  # set the login state to true
             # User authentication successful
            # Set the user ID in the session to track the login status
                request.session['user_username'] = user.username
               # Redirects to user information page, has been successfully directed.
                return redirect(reverse('home', kwargs={'nickname': user.username}))
            else:
               # Password does not match
                return HttpResponse("Password incorrectly!")
        except User.DoesNotExist:
            # Username does not exist
            return HttpResponse("User is not exist!")
    else:
       # Display the login form
        userform = UserForm()
        return render(request, 'login.html', {'userform': userform})  # Suppose you have a template called 'login.html'
@login_requiredforuser
def logout_view(request):
    # clean the session in the login state
    print("Session before pop:", dict(request.session))

    removed_value = request.session.pop('is_logged_in', None)

    if removed_value is None:
        print("is_logged_in was not set in the session.")
    else:
        print("is_logged_in was set to", removed_value, "and has been removed from the session.")

    print("Session after pop:", dict(request.session))
    request.session.save()

    response = redirect(reverse('login'))
    # Set additional cache-control headers if necessary
    response['Cache-Control'] = 'no-store'
    return response

def index(request):
   # Return the index.html template, or whatever you want to display
    return render(request, 'index.html')

def gdpr(request):
   # Return the index.html template, or whatever you want to display
    return render(request, 'gdpr.html')
