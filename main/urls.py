from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('rent', views.rent, name='conditions'),
    path('order', views.order, name='order')
]
