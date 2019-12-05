from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel

# Create your views here.
def list(request):
    latest_squirrel_list = Squirrel.objects.order_by('-id')[:5]
    output = ', '.join([q.squirrel_id for q in latest_squirrel_list])
    return HttpResponse(output)




