from django.urls import path
from .views import  bulk_upload,nearby_foodtrucks

urlpatterns = [
    path('bulk_upload/', bulk_upload, name='bulk_upload'),
    path('nearby_foodtrucks/<str:latitude>/<str:longitude>/', nearby_foodtrucks, name='nearby_foodtrucks'),
]