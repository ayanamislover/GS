from django.http import HttpResponse
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.urls import reverse


# Make sure you have imported the User and PlayerProfile models from your model files
from .models import User
from usersinformation.models import PlayerProfile
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login  # Import authenticate and login functions
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
# Define user forms
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')



# Register view

from django.contrib.auth.hashers import make_password

# 用户注册
@csrf_exempt
def regist(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)

        if userform.is_valid():
            print("开始用户注册咯:")
            # 从表单中获取数据
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']

            # 检查用户名是否唯一
            if User.objects.filter(username=username).exists():
                # 如果用户名已存在，向表单添加错误
                userform.add_error('username', 'The username is already taken. Please choose another one.')
                return render(request, 'regist.html', {'userform': userform})

            # 哈希密码
            hashed_password = make_password(password)

            # 修改了创建的顺序
            pp = PlayerProfile.objects.create(email=email, nickname=username)
            print("创建好了用户详情：", pp)
            user = User.objects.create(username=username, password=hashed_password, email=email, player_profile=pp)
            print("创建好了用户：", user)

            # 创建新用户
            # user = User.objects.create(username=username, password=hashed_password, email=email)
            # 创建与新用户关联的PlayerProfile实例
            # PlayerProfile.objects.create(user=user, email=email, nickname=username)

            # 注册成功后，重定向到登录界面
            return redirect(reverse('login'))
        else:
            print("表单无效")
            # 如果表单无效，用已填充的信息重新渲染注册页面
            return render(request, 'regist.html', {'userform': userform})
    else:
        # 对于GET请求或其他非POST请求，显示一个空的注册表单
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
            return HttpResponse("username Invalid login用户不存在")
    else:
       # Display the login form
        userform = UserForm()
        return render(request, 'login.html', {'userform': userform})  # Suppose you have a template called 'login2.html'

def index(request):
   # Return the index.html template, or whatever you want to display
    return render(request, 'index.html')