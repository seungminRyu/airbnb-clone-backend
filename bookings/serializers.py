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

    def validate(self, data):
        check_in = data["check_in"]
        check_out = data["check_out"]

        if check_in > check_out:
            raise serializers.ValidationError(
                "Check in Time can't be late then check out time"
            )

        if Booking.objects.filter(
            check_in__lte=check_out,
            check_out__gte=check_in,
        ).exists():
            raise serializers.ValidationError("These dates are already taken")

        return data
