from rest_framework.serializers import ModelSerializer
from .models import User


class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "avatar", "username")


class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "is_active",
            "groups",
            "first_name",
            "last_name",
            "is_staff",
            "is_superuser",
            "id",
            "user_permissions",
        ]
