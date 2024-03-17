from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html

from .models import Photo

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['image', 'uploaded_at', 'location']  # 加入地点字段
    list_filter = ['uploaded_at', 'location']  # 加入地点过滤
    readonly_fields = ['image_tag', ]  # 注意，如果你想在详情页也显示图片，加上这行

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" height="auto" />', obj.image.url)
        return None

    image_tag.short_description = 'Image'
