from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views
from foodtruck.views import home
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions



schema_view = get_schema_view(
    openapi.Info(
        title="Base API",
        default_version="v1",
        description="API endpoints for Base API Course",
        contact=openapi.Contact(email="utkarsh.in09@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/user/', include('account.urls')),
    path('foodtruck/', include('foodtruck.urls')),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
