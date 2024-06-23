from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views
from foodtruck.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/user/', include('account.urls')),
    path('foodtruck/', include('foodtruck.urls')),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
