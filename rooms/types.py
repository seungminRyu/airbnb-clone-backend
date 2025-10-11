from typing import List, Optional
from django.conf import settings
import strawberry
from strawberry import auto
from strawberry.types import Info
from . import models
from wishlists.models import Wishlist
from users.types import UserType
from reviews.types import ReviewType


@strawberry.django.type(models.Room)
class RoomType:
    id: auto
    name: auto
    kind: auto
    owner: "UserType"

    @strawberry.field
    def reviews(self, page: Optional[int] = 1) -> List["ReviewType"]:
        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = page * page_size
        return self.reviews.all()[start:end]

    @strawberry.field
    def rating(self) -> str:
        return self.rating()

    @strawberry.field
    def is_owner(self, info: Info) -> bool:
        return self.owner == info.context.request.user

    @strawberry.field
    def is_liked(self, info: Info) -> bool:
        user = info.context.request.user
        return Wishlist.objects(
            user=user,
            room__pk=self.pk,
        ).exists()
