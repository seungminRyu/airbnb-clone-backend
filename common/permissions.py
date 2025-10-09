from typing import Any
from strawberry.permission import BasePermission
from strawberry.types import Info


class OnlyLoggedIn(BasePermission):

    message = "You need to be logged in to access"

    def has_permission(self, source: Any, info: Info):
        return info.context.request.user.is_authenticated
