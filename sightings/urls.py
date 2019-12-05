from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    # path('<squirrel_id>/', views.update, name='update'),
        ]
