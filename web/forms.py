
from django import forms
class UserForm(forms.Form):#继承表单
    username = forms.CharField( max_length=50)
    password = forms.CharField( widget=forms.PasswordInput())
    email = forms.EmailField()