from django.shortcuts import render
from sightings.models import Squirrel
from django.http import HttpResponse


def default_map(request):
    sightings = Squirrel.objects.all()

    context = {'sightings':sightings}
    return render(request,'map/map.html',context)

def index(request):
return HttpResponse(‘Hi!How are you’)

