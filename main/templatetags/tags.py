from django import template
from ..models import Cart, Costume, FinishedOrders

register = template.Library()


@register.filter
def id(name):
    return Costume.objects.get(name=name).id


@register.filter
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


@register.filter
def cost_count(name, quantity):
    price = Costume.objects.get(name=name).price
    return int(quantity) * int(price)

@register.filter
def date(name):
    obj = FinishedOrders