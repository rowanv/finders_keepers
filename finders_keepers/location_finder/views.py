from django.shortcuts import render


def index(request):
    '''
    Display main app.

    **Template**:
    :template:`index.html`
    '''
    return render(request, 'index.html')