from rest_framework.exceptions import ParseError
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from users.serializers import PrivateUserSerializer


class Users(APIView):
    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError

        serializer = PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            new_user.set_password(password)
            Response(
                PrivateUserSerializer(new_user).data,
                status=HTTP_200_OK,
            )
        else:
            Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PrivateUserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = PrivateUserSerializer(
            request.user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_user = serializer.save()
            Response(
                PrivateUserSerializer(updated_user).data,
                status=HTTP_200_OK,
            )
        else:
            Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )
