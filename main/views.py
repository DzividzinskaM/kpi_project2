from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def order(request):
    return render(request, 'order.html')


def rent(request):
    return render(request, 'conditions.html')


def main(request):
    return render(request, 'index.html', {'alert': 1})


def cart(request):
    return render(request, 'cart.html')


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # fname = request.POST.get('fname')
        # lname = request.POST.get('lname')
        login = request.POST.get('login')
        password = request.POST.get('password')
        # re_pass = request.POST.get('repeatPassword')
        # phonenumber = request.POST.get('phoneNumber')
        # email = request.POST.get('mail')
        err = ''
        if form.is_valid():
            form.save()
            user = authenticate(request, username=login, password=password)
            auth_login(request, user)
            user = request.user
            return render(request, 'index.html', {'success': 1, 'is_auth': user})
        else:
            if form:
                for i in form:
                    if i.errors:
                        err = i.errors
                        break
            return render(request, 'registration.html', {'err': err})
    return render(request, 'registration.html')


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return render(request, 'index.html', {'login_success': 1})
    return render(request, 'login.html', {'login_success': 0})


def logout_view(request):
    logout(request)
    return redirect('/login')
