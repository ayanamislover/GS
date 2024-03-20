from datetime import datetime
from decorate import login_requiredforuser
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import forms
@login_requiredforuser
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
@login_requiredforuser
def upload_view(request,nickname):
    if request.method == "GET":
        return render(request, "upload.html", {"nickname":nickname})
