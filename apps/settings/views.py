from django.shortcuts import render
from apps.settings.models import Settings
# Create your views here.

def index(request):
    settings = Settings.objects.latest('id')
    return render(request, 'index.html', {'settings': settings})

def about(request):
    settings = Settings.objects.latest('id')
    return render(request, 'about.html', {'settings': settings})

def contact(request):
    settings = Settings.objects.latest('id')
    return render(request, 'contact.html', {'settings': settings})
