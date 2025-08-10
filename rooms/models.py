from django.db import models
from django.db.models.aggregates import Avg
from common.models import CommonModel


class Room(CommonModel):
    """Room Model Definition"""

    class RoomKindChoice(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "ENTIRE_PLACE")
        PRIVATE_ROOM = ("private_room", "PRIVATE_ROOM")
        SHARED_ROOM = ("shared_room", "SHARED_ROOM")

    name = models.CharField(max_length=180, default="")
    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(max_length=20, choices=RoomKindChoice.choices)
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="rooms"
    )
    amenities = models.ManyToManyField("rooms.Amenity", related_name="rooms")

    def __str__(room) -> str:
        return room.name

    def total_amenities(room):
        return room.amenities.count()

    def rating(room):
        count = room.reviews.count()
        if count == 0:
            return "No Reviews"
        else:
            # 니꼬 ver
            # total_rating = 0
            # for review in room.reviews.all().values("rating"):
            #     total_rating += review["rating"]
            # return round(total_rating / count, 2)

            # 개선 ver
            avg_rating = room.reviews.aggregate(Avg("rating"))["rating__avg"]
            return round(avg_rating)


class Amenity(CommonModel):
    """Amenity Model Definition"""

    name = models.CharField(max_length=150)
    description = models.TextField(max_length=150, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
