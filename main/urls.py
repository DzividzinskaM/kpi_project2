from django.urls import path, include
from . import views

urlpatterns = [
    path('rent', views.rent, name='conditions'),
    path('', views.main, name='index')
]
