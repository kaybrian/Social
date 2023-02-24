from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, re_path, include


schema_view = get_schema_view(
    openapi.Info(
        title="People Social Media Applications API",
        default_version='v1',
        description="THe api in used for a social application that will be used by people to post their thoughts and ideas on the platform",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="b.kayongo@alustudent.com"),
        license=openapi.License(name="MIT Licence"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
]