from django.shortcuts import render


# Create your views here.

def order(request):
    return render(request, 'order.html')


def rent(request):
    return render(request, 'conditions.html')


def main(request):
    return render(request, 'index.html')


def cart(request):
    return render(request, 'cart.html')


def registration(request):
    return render(request, 'registration.html')


def login(request):
    return render(request, 'login.html')
