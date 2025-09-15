from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response({"ok": True, "categories": serializer.data})

    elif request.method == "POST":
        kind = request.data.get("kind")
        name = request.data.get("name")
        Category.objects.create(kind=kind, name=name)
        return Response(
            {
                "created": True,
            }
        )


@api_view(["GET"])
def category(request, pk):
    if request.method == "GET":
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response({"ok": True, "category": serializer.data})
