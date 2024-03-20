from django.shortcuts import render,HttpResponse
from .models import Activity

def home(request):
    return render(request,"home.html")

def acti(request):
    activity = Activity.objects.all()
    context = {
        'activity': activity
    }
    return render(request,"activity.html", context)