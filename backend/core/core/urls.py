from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
    TokenObtainPairView,
    TokenRefreshView,
)
from django.http import JsonResponse
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


def health(request):
    return JsonResponse({"status": "ok"})


schema_view = get_schema_view(
    openapi.Info(
        title="Authors Haven API",
        default_version="v1",
        description="Api endpoints for Autors Haven API Course",
        contact=openapi.Contact(email="mygmail@gmail.com"),
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("schema.json", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("api/admin/", admin.site.urls),
    path("api/", include("job.urls")),
    path("api/account/", include("account.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="tokenverify"),
    path("health/", health),
]
