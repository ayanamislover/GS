from django.db import models

class announcenment(models.Model):
    title = models.CharField(max_length=30)#文章标题
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

