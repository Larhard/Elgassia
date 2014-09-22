from django import template

register = template.Library()


@register.simple_tag()
def title():  # TODO
    return "Elgassia"


@register.simple_tag()
def language():  # TODO
    return "en"
