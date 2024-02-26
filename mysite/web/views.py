#coding=utf-8

from django.http import HttpResponse
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm
from django.urls import reverse


# 确保你已经从你的模型文件中导入了User和PlayerProfile模型
from .models import User
from usersinformation.models import PlayerProfile
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login  # 导入authenticate和login函数

# 定义用户表单




# 注册视图

from django.contrib.auth.hashers import make_password

def regist(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            # 获取表单数据
            username = userform.cleaned_data['username']
            password = make_password(userform.cleaned_data['password'])  # 哈希密码
            email = userform.cleaned_data['email']

            # 创建新用户
            user = User.objects.create(username=username, password=password, email=email)

            # 创建与新用户关联的PlayerProfile实例
            #PlayerProfile.objects.create(user=user, email= email, nickname=username)

            # 注册成功后跳转到登录界面
            return redirect(reverse('login'))
        else:
            # 如果表单无效，重新渲染注册页面，并带上已经填写的表单信息
            return render(request, 'regist.html', {'userform': userform})
    else:
        # GET 请求或其他非POST请求，显示空的注册表单
        userform = UserForm()
        return render(request, 'regist.html', {'userform': userform})



# 登录视图
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
#from .forms import UserForm  # 确保你已经正确地导入了UserForm


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                # 用户验证成功
                # 在会话中设置用户ID来跟踪登录状态
                request.session['user_username'] = user.username
                # 重定向到用户信息页面
                return redirect(reverse('usersinformation:player_profile', kwargs={'nickname': user.username}))
            else:
                # 密码不匹配
                return HttpResponse("密码Invalid login")
        except User.DoesNotExist:
            # 用户名不存在
            return HttpResponse("用户名Invalid login")
    else:
        # 显示登录表单
        userform = UserForm()
        return render(request, 'login.html',{'userform': userform})  # 假设你有一个名为'login.html'的模板

def index(request):
    # 返回 index.html 模板，或者您希望显示的任何内容
    return render(request, 'index.html')



