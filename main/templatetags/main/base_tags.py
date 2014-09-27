from django import template
from django.core.exceptions import ObjectDoesNotExist

from main.models import Config


register = template.Library()


@register.simple_tag()
def title():
    try:
        return Config.objects.get(key='title').value
    except ObjectDoesNotExist:
        return "Title Undefined"


@register.simple_tag()
def language():  # TODO
    return "en"
