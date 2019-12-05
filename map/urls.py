from django.urls import path
from .import views

    
#urlpatterns = [
#    path('',views.index),
#]

urlpatterns = [
        path('', views.map, name='default'),
]

