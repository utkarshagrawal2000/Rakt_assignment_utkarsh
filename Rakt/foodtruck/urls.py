from django.urls import path
from .views import  bulk_upload,nearby_foodtrucks,filter_by_food_type,filter_by_zipcode

urlpatterns = [
    path('bulk_upload/', bulk_upload, name='bulk_upload'),
    path('nearby_foodtrucks/<str:latitude>/<str:longitude>/', nearby_foodtrucks, name='nearby_foodtrucks'),
    path('filter_by_food_type/<str:food_type>/', filter_by_food_type, name='filter_by_food_type'),
    path('filter_by_zipcode/<str:zipcode>/', filter_by_zipcode, name='filter_by_zipcode'),
]