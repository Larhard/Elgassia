from django.core.exceptions import ObjectDoesNotExist
from main.models import Config


def theme(request):
    try:
        default_theme = Config.objects.get(key='default_theme')
    except ObjectDoesNotExist:
        default_theme = 'prototype'
    active_theme = request.COOKIES.get('theme', default_theme)

    return {
        'active_theme': active_theme
    }