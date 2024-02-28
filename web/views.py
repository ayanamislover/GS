#coding=utf-8

from django.http import HttpResponse
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm
from django.urls import reverse


# Make sure you have imported the User and PlayerProfile models from your model files
from .models import User
from usersinformation.models import PlayerProfile
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login  # Import authenticate and login functions

# Define user forms




# Register view

from django.contrib.auth.hashers import make_password

def regist(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            # Get form data
            username = userform.cleaned_data['username']
            password = make_password(userform.cleaned_data['password'])  # Hash password
            email = userform.cleaned_data['email']

            # Create a new user
            user = User.objects.create(username=username, password=password, email=email)

            # Create a PlayerProfile instance associated with the new user
            #PlayerProfile.objects.create(user=user, email= email, nickname=username)

            # After successful registration, go to the login interface
            return redirect(reverse('login'))
        else:
           # If the form is invalid, re-render the registration page with the information of the form already filled out
            return render(request, 'regist.html', {'userform': userform})
    else:
       # GET request or other non-POST request, showing an empty registration form
        userform = UserForm()
        return render(request, 'regist.html', {'userform': userform})



# Login view
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
# from.forms import UserForm # Make sure you have imported UserForm correctly


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
             # User authentication successful
# Set the user ID in the session to track the login status
                request.session['user_username'] = user.username
               # Redirects to user information page, has been successfully directed.
                return redirect(reverse('home', kwargs={'nickname': user.username}))
            else:
               # Password does not match
                return HttpResponse("password Invalid login")
        except User.DoesNotExist:
            # Username does not exist
            return HttpResponse("username Invalid login")
    else:
       # Display the login form
        userform = UserForm()
        return render(request, 'login.html',{'userform': userform})  # Suppose you have a template called 'login.html'

def index(request):
   # Return the index.html template, or whatever you want to display
    return render(request, 'index.html')
