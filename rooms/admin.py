from django.contrib import admin, messages
from .models import Room, Amenity


@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, rooms):
    if not request.user.is_superuser:
        messages.error(request, "작업 수행 권한이 없습니다.")
        return

    updated_count = 0
    for room in rooms.all():
        room.price = 0
        room.save()
        updated_count += 1

    messages.success(request, f"{updated_count}개의 방 가격이 초기화 되었습니다.")


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """Custom Room Admin"""

    actions = (reset_prices,)

    list_display = (
        "name",
        "price",
        "rating",
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
    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     queryset = queryset.annotate(
    #         _total_reviews=Count("reviews"),
    #     )
    #     return queryset

    # def total_reviews(self, obj):
    #     return getattr(obj, "_total_reviews", obj.reviews.count())

    # total_reviews.admin_order_field = "_total_reviews"
    # total_reviews.short_description = "전체 리뷰 수"


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
