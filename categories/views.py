from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer


class Categories(APIView):
    def get(self, request):
        return get_all_categories()

    def post(self, request):
        return create_category(request.data)


class CategoryDetail(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        category = self.get_object(pk)
        return get_category(instance=category)

    def put(self, request, pk):
        category = self.get_object(pk)
        return update_category(instance=category, data=request.data)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)


def get_all_categories():
    all_categories = Category.objects.all()
    serializer = CategorySerializer(all_categories, many=True)
    return Response({"ok": True, "categories": serializer.data})


def create_category(data):
    serializer = CategorySerializer(data=data)
    if serializer.is_valid():
        new_category = serializer.save()
        return Response(CategorySerializer(new_category).data)
    else:
        return Response(serializer.errors)


def get_category(instance):
    serializer = CategorySerializer(instance)
    return Response(serializer.data)


def update_category(instance, data):
    serializer = CategorySerializer(instance, data=data, partial=True)
    if serializer.is_valid():
        updated_category = serializer.save()
        return Response(CategorySerializer(updated_category).data)
    else:
        return Response(serializer.errors)
