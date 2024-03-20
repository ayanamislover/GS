from django.db import models


class Activity(models.Model):
    """
    An activity model
    """
    title = models.CharField(max_length=120)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    max_participants = models.PositiveIntegerField()
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('draft', 'Draft 草稿'), ('published', 'Published 发布'), ('ended', 'Ended 结束')], default='draft')
    organizer = models.CharField(max_length=120)
    category = models.CharField(max_length=50)
    tags = models.CharField(max_length=255, blank=True, null=True)
    series_id = models.CharField(max_length=100, unique=True)
