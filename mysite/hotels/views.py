from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from .models import Hotel

# Create your views here.
longitude = -80.191788
latitude = 25.761681

user_coordinate = Point(longitude, latitude, srid=4326)

class HotelListView(generic.ListView):
    model = Hotel
    context_object_name = 'hotels'
    queryset = Hotel.objects.annotate(distance=Distance('location', user_coordinate)).order_by('distance')[0:6]



