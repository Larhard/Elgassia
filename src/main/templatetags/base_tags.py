from django import template

register = template.Library()


@register.simple_tag(name='title')
def title():
    return "Elgassia"
