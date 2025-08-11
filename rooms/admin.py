from django.contrib import admin
from django.db.models.aggregates import Count
from .models import Room, Amenity


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """Custom Room Admin"""

    list_display = (
        "name",
        "price",
        "rating",
        "total_reviews",
        "kind",
        "total_amenities",
        "owner",
        "created_at",
    )
    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "name",
        "^price",
        "=owner__username",
    )
    readonly_fields = ("rating",)

    # total_reviews가 오름,내림 정렬 될 수 있도록
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _total_reviews=Count("reviews"),
        )
        return queryset

    def total_reviews(self, obj):
        return getattr(obj, "_total_reviews", obj.reviews.count())

    total_reviews.admin_order_field = "_total_reviews"
    total_reviews.short_description = "전체 리뷰 수"


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    """Custom Amenity Admin"""

    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
