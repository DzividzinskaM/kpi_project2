from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('rent', views.rent, name='conditions'),
    path('order', views.order, name='order'),
    path('cart', views.cart, name='cart'),
    path('registration', views.registration, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]
