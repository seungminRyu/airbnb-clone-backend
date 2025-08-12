from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "단어 포함"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("좋아요", "Good"),
            ("최고에요", "Great"),
            ("대박이에요", "Awesome"),
        ]

    def queryset(self, request, reviews):
        value = self.value()
        if value:
            return reviews.filter(payload__contains=value)
        else:
            return reviews


class RatingRangeFilter(admin.SimpleListFilter):
    title = "평점 범위"
    parameter_name = "rating_range"

    def lookups(self, request, model_admin):
        return [
            ("high", "높은 평점 (4-5점)"),
            ("medium", "보통 평점 (3-4점)"),
            ("low", "낮은 평점(1-2점)"),
        ]

    def queryset(self, request, reviews):
        range_value = self.value()
        if range_value == "high":
            return reviews.filter(rating__gte=4)
        elif range_value == "medium":
            return reviews.filter(rating__gte=3, rating__lt=4)
        elif range_value == "low":
            return reviews.filter(rating__lt=3)
        return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "rating",
        "room",
        "experience",
        "payload",
    )
    list_filter = (
        WordFilter,
        RatingRangeFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
