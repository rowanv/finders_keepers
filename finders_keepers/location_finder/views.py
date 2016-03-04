import yaml
from django.shortcuts import render
from django.conf import settings



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