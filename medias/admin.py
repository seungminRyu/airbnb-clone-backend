from django.contrib import admin
from .models import Video, Photo


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
