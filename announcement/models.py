from django.db import models

class announcement(models.Model):
    title = models.CharField(max_length=30)#文章标题
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title