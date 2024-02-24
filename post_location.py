from django.shortcuts import render
#from .models import Activity

def map_view(request, target_location=None):

    #target_location = Activity.Location.first()
    target_latitude = 50.7260
    target_longitude = -3.5275
    context = {
        'target_latitude': target_latitude,
        'target_longitude': target_longitude,
    }
    return render(request, 'map_template.html', context)
