from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "rating",
        "room",
        "experience",
        "payload",
    )
    list_filter = ("rating",)
