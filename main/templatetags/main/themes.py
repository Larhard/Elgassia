from django import template
import os

from elgassia.settings import STATIC_ROOT


register = template.Library()


class ThemesList(template.Node):
    def render(self, context):
        themes = []
        try:
            themes += os.listdir(os.path.join(STATIC_ROOT, 'css/themes'))
        except OSError:
            pass
        context['themes_list'] = themes
        return ''


# noinspection PyUnusedLocal
@register.tag
def get_themes_list(parser, token):
    return ThemesList()

