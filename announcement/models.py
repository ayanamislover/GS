from django.db import models
from django.utils import timezone

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_start = models.DateTimeField(default=timezone.now)
    end_data = models.DateTimeField()
    image = models.ImageField(upload_to='announcement_images/',default='path/to/default/image.jpg')




    def __str__(self):
        return self.title