from django import template
<<<<<<< HEAD
from ..models import Cart, Costume
=======
from ..models import Cart, Costume, FinishedOrders
>>>>>>> backend

register = template.Library()


@register.filter
<<<<<<< HEAD
=======
def id(name):
    return Costume.objects.get(name=name).id


@register.filter
>>>>>>> backend
def about(name):
    return Costume.objects.get(name=name).about


@register.filter
def count(name):
    return Costume.objects.get(name=name).count


@register.filter
def price(name):
    return Costume.objects.get(name=name).price


@register.filter
def image(name):
    return Costume.objects.get(name=name).image
<<<<<<< HEAD
=======


@register.filter
def cost_count(name, quantity):
    price = Costume.objects.get(name=name).price
    return int(quantity) * int(price)

@register.filter
def date(name):
    obj = FinishedOrders
>>>>>>> backend
