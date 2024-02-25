#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.shortcuts import render


from .models import User  # 修改导入路径

# 定义用户表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')



# 注册视图
def regist(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']
            # 创建新用户
            user = User.objects.create(username=username, password=password, email=email)
            # 对于create方法，不需要再调用save()，因为create()已经保存了实例
            return HttpResponse('regist success!!!')
    else:
        userform = UserForm()
    return render(request, 'regist.html', {'userform': userform})



# 登录视图
def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']

            # 验证用户名和密码
            user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                return render(request, 'index.html', {'username': username})
            else:
                return HttpResponse('User name or password is wrong, please log in again.')

    else:
        userform = UserForm()
    return render(request, 'login.html', {'userform': userform})

def index(request):
    # 返回 index.html 模板，或者您希望显示的任何内容
    return render(request, 'index.html')