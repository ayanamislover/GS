import os
import uuid

from django.db import models


def custom_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return f"photos/{new_filename}"


class Photo(models.Model):
    # image = models.ImageField(upload_to='photos/')
    image = models.ImageField(upload_to=custom_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255, blank=True, null=True)  # 添加地点字段
