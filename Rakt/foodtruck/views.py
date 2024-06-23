from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from .models import FoodTruck
from io import StringIO
import csv
from .serializers import FileUploadSerializer,FoodTruckSerializer
from django.db.models import  F
from django.db.models.functions import Power, Sqrt

@api_view(['POST'])
@parser_classes([MultiPartParser])
def bulk_upload(request):
    serializer = FileUploadSerializer(data=request.data)
    if serializer.is_valid():
        csv_file = request.FILES['file']
        file_text = csv_file.read().decode('utf-8')
        csv_reader = csv.DictReader(StringIO(file_text))
        
        food_truck_objects = []
        locationids = set(FoodTruck.objects.values_list('locationid', flat=True))  
        new_locationids = set()

        for row in csv_reader:
            if not row['X']:
                row['X'] = None
            if not row['Y']:
                row['Y'] = None

            locationid = row.get('locationid')  
            if locationid in locationids or locationid in new_locationids:
                continue 

            new_locationids.add(locationid)
            food_truck_objects.append(FoodTruck(
                locationid=row.get('locationid'),
                applicant=row.get('Applicant'),
                facility_type=row.get('FacilityType'),
                cnn=row.get('cnn'),
                location_description=row.get('LocationDescription'),
                address=row.get('Address'),
                blocklot=row.get('blocklot'),
                block=row.get('block'),
                lot=row.get('lot'),
                permit=row.get('permit'),
                status=row.get('Status'),
                food_items=row.get('FoodItems'),
                x=row['X'],
                y=row['Y'],
                latitude=row.get('Latitude'),
                longitude=row.get('Longitude'),
                schedule=row.get('Schedule'),
                dayshours=row.get('dayshours'),
                nois_sent=row.get('NOISent'),
                approved=row.get('Approved'),
                received=row.get('Received'),
                prior_permit=row.get('PriorPermit'),
                expiration_date=row.get('ExpirationDate'),
                location=row.get('Location'),
                fire_prevention_districts=row.get('Fire Prevention Districts'),
                police_districts=row.get('Police Districts'),
                supervisor_districts=row.get('Supervisor Districts'),
                zip_codes=row.get('Zip Codes'),
                neighborhoods=row.get('Neighborhoods (old)'),
            ))

        try:
            FoodTruck.objects.bulk_create(food_truck_objects)
            return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def nearby_foodtrucks(request,latitude=None,longitude=None):
    latitude = float(latitude)
    longitude = float(longitude)
    nearby_trucks = FoodTruck.objects.annotate(
        distance=Sqrt(Power(F('latitude') - latitude, 2) + Power(F('longitude') - longitude, 2))
    ).order_by('distance')[:5]
    print(nearby_trucks)
    print(type(nearby_trucks))
    serializer = FoodTruckSerializer(nearby_trucks, many=True)
    return Response(serializer.data)