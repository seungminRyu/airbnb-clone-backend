from django.db import models
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
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    amenities = models.ManyToManyField("rooms.Amenity")

    def __str__(self) -> str:
        return self.name


class Amenity(CommonModel):
    """Amenity Definition"""

    name = models.CharField(max_length=150)
    description = models.TextField(max_length=150, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
