from django.shortcuts import render


# Create your views here.


def rent(request):
    return render(request, 'conditions.html')


def main(request):
    return render(request, 'index.html')
