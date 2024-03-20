from django.shortcuts import render,HttpResponse
from .models import Activity
from decorate import login_requiredforuser

@login_requiredforuser
def home(request):
    return render(request,"home.html")
@login_requiredforuser
def acti(request):
    activity = Activity.objects.all()
    context = {
        'activity': activity
    }
    return render(request,"activity.html", context)