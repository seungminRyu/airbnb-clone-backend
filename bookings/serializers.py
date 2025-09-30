from rest_framework import serializers
from django.utils import timezone
from .models import Booking


class PublicBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "pk",
            "check_in",
            "check_out",
            "experience_time",
            "guests",
        ]


class CreateRoomBookingSerializer(serializers.ModelSerializer):

    check_in = serializers.DateField()
    check_out = serializers.DateField()

    class Meta:
        model = Booking
        fields = [
            "check_in",
            "check_out",
            "guest",
        ]

    def validate_check_in(self, value):
        now = timezone.localtime(timezone.now()).date()

        if now > value:
            raise serializers.ValidationError("Can't book in the past")
        else:
            return value

    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()

        if now > value:
            raise serializers.ValidationError("Can't book in the past")
        else:
            return value
