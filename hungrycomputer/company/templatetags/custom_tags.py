from django import template

register = template.Library()

@register.filter
def plus(value, arg):
    value = value + 1
    print(type(value))
    return value * arg

