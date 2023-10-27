from django.contrib import admin
from django.urls import path, include
from core import views
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Livraria API",
        default_version='v1',
        description="",
        terms_of_service="https://www.livros.com/api/",
        contact=openapi.Contact(email="email"),
        license=openapi.License(name="name"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    #generator_class=SwaggerAutoSchema,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include('core.urls')),
]