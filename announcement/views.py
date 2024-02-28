from django.shortcuts import render, get_object_or_404

from .models import Announcement  # Make sure to import Announcement from your models file

def list(request):
    announcements = Announcement.objects.order_by('date_start')
    return render(request, 'announcement/list.html', {'announcements': announcements})

def detail(request, title):
    # Use get_object_or_404 to get a specific announcement or return a 404 error
    announcement = get_object_or_404(Announcement, title=title)
    return render(request, "announcement/detail.html", {'announcement': announcement})

