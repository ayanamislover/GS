from django.shortcuts import render, HttpResponse
from .models import Activity
from decorate import login_requiredforuser

# This decorator checks if the user is logged in before allowing access to the view.
@login_requiredforuser
def home(request):
    # Renders and returns the home page template.
    return render(request, "home.html")

# Another view that requires the user to be logged in.
@login_requiredforuser
def acti(request):
    # Retrieves all instances of Activity from the database.
    activity = Activity.objects.all()
    context = {
        'activity': activity  # Adds the list of activities to the context for rendering in the template.
    }
    # Renders and returns the activity page template with the context.
    return render(request, "activity.html", context)
