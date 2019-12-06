from django.shortcuts import render
from django.http import HttpResponse
from sightings.models import Squirrel

#def index(request):
#    return HttpResponse('Hi!How are you')

def map(request):
    sightings = Squirrel.objects.all()
    context = {'sightings': sightings}
    return render(request, 'map.html', context)

# Create your views here.
