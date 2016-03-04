import yaml
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import json

from location_finder.models import Location

API_KEY = getattr(settings, "API_KEY", '')


def index(request):
    '''
    Display main app.
    **Context**:
    api_key: Google Maps API key

    **Template**:
    :template:`index.html`
    '''
    return render(request, 'index.html', {'api_key': API_KEY})

def edit_location(request):
    '''
    '''
    if request.is_ajax():
        location_data = json.loads(request.body.decode('utf-8'))
        new_location = Location(
            lat=location_data['lat'],
            lon=location_data['lon'],
            address=location_data['address'])
        new_location.save()
        return HttpResponse('you added a Location')