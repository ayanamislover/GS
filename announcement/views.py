from django.shortcuts import render, get_object_or_404
from decorate import login_requiredforuser
from .models import Announcement  # Make sure to import Announcement from your models file
@login_requiredforuser
def list(request):
    announcements = Announcement.objects.order_by('date_start')
    return render(request, 'announcement/list.html', {'announcements': announcements})
@login_requiredforuser
def detail(request, title):
    # Use get_object_or_404 to get a specific announcement or return a 404 error
    announcement = get_object_or_404(Announcement, title=title)
    return render(request, "announcement/detail.html", {'announcement': announcement})

