import yaml
from django.shortcuts import render, redirect
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
    print(Location.objects.all())
    return render(request, 'index.html',
                  {'api_key': API_KEY,
                   'all_locations': Location.objects.all()})


def edit_location(request):
    '''
    '''
    if request.is_ajax():
        print(request.body)
        print(dir(request))
        print(request.POST['lat'])
        new_location = Location(
            # Type conversion here to avoid utf-8 error
            lat=float(request.POST['lat']),
            lon=float(request.POST['lon']),
            address=request.POST['address'])
        new_location.save()
        return HttpResponse('you added a Location')


def delete_all_locations(request):
    '''
    '''
    if request.method == 'POST':
        Location.objects.all().delete()
        return redirect('index')
