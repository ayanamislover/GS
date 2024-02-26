from django.db import models
from django.utils import timezone

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_start = models.DateTimeField(default=timezone.now)
    end_data = models.DateTimeField()

    def __str__(self):
        return self.title