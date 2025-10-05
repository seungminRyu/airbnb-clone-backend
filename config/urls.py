from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from strawberry.django.views import GraphQLView
from .schema import schema
from config.settings import MEDIA_ROOT

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/rooms/", include("rooms.urls")),
    path("api/v1/categories/", include("categories.urls")),
    path("api/v1/experiences/", include("experiences.urls")),
    path("api/v1/medias/", include("medias.urls")),
    path("api/v1/wishlists/", include("wishlists.urls")),
    path("api/v1/users/", include("users.urls")),
    path("api/v1/users/", include("users.urls")),
    path("graphql", GraphQLView.as_view(schema=schema)),
] + static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
