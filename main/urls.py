from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('rent', views.rent, name='conditions'),
    path('order', views.order, name='order'),
    path('cart', views.cart, name='cart'),
    path('registration', views.registration, name='register'),
    path('cabinet', views.cabinet, name='cabinet'),
    path('login', views.login, name='login'),
    path('logout', views.logout_view, name='logout'),
<<<<<<< HEAD
    path('add', views.add, name='add'),
    path('<str:name>', views.item_window, name='window')
=======
    path('create', views.create, name='create'),
    path('cart_update', views.cart_update, name='cart_update'),
    path('remove', views.remove, name='remove'),
    path('cart_order', views.cart_order, name='cart_order'),
    path('<int:id>', views.item_window, name='window')
>>>>>>> backend
]
