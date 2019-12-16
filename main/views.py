from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Costume, Cart
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def remove(request):
    if request.is_ajax():
        id = request.POST.get('id')
        val = request.POST.get('val')
        cos = Costume.objects.get(id=id)
        cart = Cart.objects.get(user=request.user.username)
        del cart.items[cos.name]
        cart.cost = cart_cost(cart.items)
        x = cart.cost
        cart.save()
        cos.count += 1
        cos.save()
        return JsonResponse({'success': 1, 'total': x})
    else:
        return HttpResponse('404')


# @csrf_exempt
# def count_match(request):
#     userinput = request.POST.get('userinput')
#     cart = Cart.objects.get(user=request.user.username)
#     x = cart.cost
#     print(cart.cost)
#     cart.save()
#     if request.is_ajax():
#
#         return JsonResponse(data)

@csrf_exempt
def cart_order(request):
    cart = Cart.objects.get(user=request.user.username)
    for i, j in cart.items.items():
        cos = Costume.objects.get(name=i)
        cos.count -= int(j)
        cos.save()
    cart.delete()
    return redirect('/cart')


@csrf_exempt
def cart_update(request):
    if request.is_ajax():
        count = request.POST.get('count')
        name = request.POST.get('name')
        cart = Cart.objects.get(user=request.user.username)
        items = cart.items
        items[name] = count
        cost = cart_cost(cart.items)
        print(items)
        data = {'items': items, 'total': cost}
        cart.cost = cost
        cart.save()
        return JsonResponse(data)


@csrf_exempt
def item_window(request, id):
    if request:
        obj = Costume.objects.get(id=id)
        try:
            cart = Cart.objects.get(user=request.user.username).items
        except Cart.DoesNotExist:
            cart = {}
        return render(request, 'custom.html', {'costume': obj, 'user': request.user, 'cart': cart})


def order(request):
    return render(request, 'order.html')


def rent(request):
    return render(request, 'conditions.html')


def main(request):
    costumes = Costume.objects.all()
    return render(request, 'index.html', {'costumes': costumes})


@csrf_exempt
def cart(request):
    user_id = request.user.username
    print(user_id)
    data = {}
    costumes_json = {}
    try:
        obj = Cart.objects.get(user=user_id)
        data = obj.items
        print(data)
        for i, j in data.items():
            costumes = Costume.objects.get(name=i)
            costumes_json[costumes.name] = {
                'count': costumes.count,
                'price': costumes.price,
                'image': costumes.image,
                'cost_display': costumes.count * costumes.price
            }

        print(costumes_json)
        return render(request, 'cart.html', {'data': data, 'costumes': costumes_json, 'totalcartcost': obj.cost})
    except Exception as e:
        print(e)
        return render(request, 'cart.html', {'data': data})


@csrf_exempt
def create(request):
    cos = Costume.objects.get(id=request.POST.get('id'))
    if request.is_ajax():
        if cos.count > 0:
            data = {}
            try:
                obj = Cart.objects.get(user=request.user.username)
                data = obj.items
                data[cos.name] = 1
                cos.count -= 1
                obj.cost += cos.price
                obj.items = data
                obj.save()
            except Cart.DoesNotExist:
                print('=========')
                data[cos.name] = 1
                cos.count -= 1
                obj = Cart.objects.create(user=request.user.username, items=data,
                                          cost=cos.price)
            finally:
                cos.save()
                data = {'Costume': cos.name, 'Count': cos.count}
                return JsonResponse(data)
        else:
            data = {'Costume': cos.name, 'Count': cos.count}
            return JsonResponse(data)


# @csrf_exempt
# def add(request):
#     if request.is_ajax():
#         i = request.POST.get('id')
#         data = {
#             'addedCostume': True
#         }
#         return JsonResponse(data)
#     else:
#         print('wefowiejfoweijfoweifjoweifjoweifwo')


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


# price of whole cart
def cart_cost(cart_item):
    cost = 0
    for i, j in cart_item.items():
        obj = Costume.objects.get(name=i)
        cost += obj.price * int(j)
    return cost
