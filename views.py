from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import forms

@csrf_exempt
def upload_api(request):
    if request.method == "POST":
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({"ok": True})
        else:
            print(form.errors)

    return JsonResponse({"ok": False})

def upload_view(request):
    if request.method == "GET":
        return render(request, "upload.html")
