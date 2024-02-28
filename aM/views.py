from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,"home.html")

def acti(request):
    return render(request,"activity.html")