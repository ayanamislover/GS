from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.urls import path
from .models import Achievement



from django.contrib import messages

# Create your views here.
#Achievement system detail screen view
def detail(request, pk):
    # Getting an Achievement instance by nickname
    achievement_detail = get_object_or_404(Achievement, pk=pk)
    # Pass the fetched user information to the template
    return render(request, "achievement/achievement_detail.html", {"achievement_detail": achievement_detail})


def achievement_detail(request):
    # Get all achievements
    achievement_detail = Achievement.objects.all()
    return render(request, "achievement/achievement_detail.html", {'achievement_detail': achievement_detail})

