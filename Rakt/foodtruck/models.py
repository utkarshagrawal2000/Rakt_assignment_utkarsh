from django.db import models

class FoodTruck(models.Model):
    locationid = models.CharField(max_length=100)
    applicant = models.CharField(max_length=100)
    facility_type = models.CharField(max_length=100)
    cnn = models.CharField(max_length=100)
    location_description = models.TextField()
    address = models.CharField(max_length=200)
    blocklot = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    lot = models.CharField(max_length=100)
    permit = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    food_items = models.TextField()
    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    schedule = models.TextField()
    dayshours = models.CharField(max_length=200,null=True, blank=True)
    nois_sent = models.CharField(max_length=100,null=True, blank=True)
    approved = models.CharField(max_length=100,null=True, blank=True)
    received = models.CharField(max_length=100,null=True, blank=True)
    prior_permit = models.CharField(max_length=100,null=True, blank=True)
    expiration_date = models.CharField(max_length=100,null=True, blank=True)
    location = models.CharField(max_length=100)
    fire_prevention_districts = models.CharField(max_length=100)
    police_districts = models.CharField(max_length=100)
    supervisor_districts = models.CharField(max_length=100)
    zip_codes = models.CharField(max_length=100)
    neighborhoods = models.CharField(max_length=100)