from django.db import models
from common.models import CommonModel


class ChattingRoom(CommonModel):
    """Chatting Room Model Definition"""

    users = models.ManyToManyField(
        "users.User",
    )

    def __str__(self) -> str:
        return "Chatting Room"


class Message(ChattingRoom):
    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    room = models.ForeignKey(
        "ChattingRoom", on_delete=models.CASCADE, related_name="messages"
    )

    def __str__(self) -> str:
        return f"{self.name} says: {self.text}"
