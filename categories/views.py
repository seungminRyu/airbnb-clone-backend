from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Category
from .serializers import CategorySerializer


@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":
        return get_all_categories()

    elif request.method == "POST":
        return create_category(request.data)


@api_view(["GET", "PUT"])
def category(request, pk):
    category = get_category(pk)

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == "PUT":
        return update_category(pk, request.data)


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


def get_category(pk):
    try:
        category = Category.objects.get(pk=pk)
        return category
    except Category.DoesNotExist:
        raise NotFound


def update_category(pk, data):
    category = get_category(pk)
    serializer = CategorySerializer(category, data=data, partial=True)
    if serializer.is_valid():
        updated_category = serializer.save()
        return Response(CategorySerializer(updated_category).data)
    else:
        return Response(serializer.errors)
