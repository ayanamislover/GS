from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def player_profile(request):
    return HttpResponse("Hello. Your are in the player profile.")