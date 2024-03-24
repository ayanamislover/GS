from django.db import models

from django.db import models


class Activity(models.Model):
    """
    Defines the Activity model which represents an event or activity within the system.
    Each activity includes details like title, content, scheduling information, location,
    and other relevant details to describe the event.
    """
    # The title of the activity.
    title = models.CharField(max_length=120)

    # A detailed description of the activity.
    content = models.TextField()

    # The date and time when the activity was published.
    publish_date = models.DateTimeField(auto_now_add=True)

    # The starting date and time for the activity.
    start_date = models.DateTimeField()

    # The ending date and time for the activity.
    end_date = models.DateTimeField()

    # Location where the activity will take place.
    location = models.CharField(max_length=255)

    # Maximum number of participants allowed.
    max_participants = models.PositiveIntegerField()

    # The fee to participate in the activity.
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    # Current status of the activity (e.g., draft, published, ended).
    status = models.CharField(max_length=20, choices=[('draft', 'Draft 草稿'), ('published', 'Published 发布'),
                                                      ('ended', 'Ended 结束')], default='draft')

    # The organizer of the activity.
    organizer = models.CharField(max_length=120)

    # The category of the activity (for classification purposes).
    category = models.CharField(max_length=50)

    # Tags associated with the activity for search and categorization.
    tags = models.CharField(max_length=255, blank=True, null=True)

    # A unique identifier for the activity, especially useful if the activity is part of a series.
    series_id = models.CharField(max_length=100, unique=True)

