from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from .models import Photo


class PhotoDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            return NotFound

    def delete(self, request, pk):
        photo = self.get_object(pk=pk)
        photo_owner = photo.room.owner if photo.room else photo.experience.host
        if photo_owner != request.user:
            raise PermissionDenied
        photo.delete()
        return Response(status=HTTP_200_OK)
