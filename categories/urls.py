from django.urls import path
from .views import CategoryViewSets

urlpatterns = [
    path("", CategoryViewSets.as_view({"get": "list", "post": "create"})),
    path(
        "<int:pk>",
        CategoryViewSets.as_view(
            {"get": "retrieve", "put": "partial_update", "delete": "destroy"}
        ),
    ),
]
