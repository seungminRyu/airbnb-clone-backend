from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError
from rest_framework.status import HTTP_204_NO_CONTENT
from django.db import transaction

from .models import Amenity, Room
from .serializers import AmenitySerializer, RoomDetailSerializer, RoomListSerializer
from categories.models import Category


class Amenities(APIView):

    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)

        if serializer.is_valid():
            new_amenity = serializer.save()
            return Response(AmenitySerializer(new_amenity).data)
        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):
    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            return NotFound

    def get(self, request, pk):
        serializer = AmenitySerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = AmenitySerializer(
            self.get_object(pk), data=request.data, partial=True
        )

        if serializer.is_valid():
            updated_amenity = serializer.save()
            return Response(AmenitySerializer(updated_amenity).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Rooms(APIView):
    def get(self, request):
        # all_rooms = Room.objects.all()

        # select_related로 ForeignKey 최적화
        # prefetch_related로 ManyToMany 최적화
        all_rooms = (
            Room.objects.select_related("owner", "category")
            .prefetch_related("amenities")
            .all()
        )

        serializer = RoomListSerializer(all_rooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return NotAuthenticated

        serializer = RoomDetailSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)

        category_pk = request.data.get("category")
        if not category_pk:
            raise ParseError("Category is required.")

        try:
            category = Category.objects.get(pk=category_pk)
            if category.kind == Category.CategoryKindChoices.EXPERIENCES:
                raise ParseError("The category kind should be 'rooms'.")
        except Category.DoesNotExist:
            raise ParseError("Category not found")

        try:
            with transaction.atomic():
                new_room = serializer(owner=request.user, category=category)
                amenities = request.data.get("amenities")

                for amenity_pk in amenities:
                    amenity = Amenity.objects.get(pk=amenity_pk)
                    new_room.amenities.add(amenity)
                serializer = RoomDetailSerializer(new_room)
                return Response(serializer.data)
        except Exception:
            raise ParseError("Amenity not found")


class RoomDetail(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            return Response(NotFound)

    def get(self, request, pk):
        try:
            room = self.get_object(pk)
            serializer = RoomDetailSerializer(room)
            return Response(serializer.data)
        except Room.DoesNotExist:
            return NotFound
