from django import template
import os

from elgassia.settings import STATICFILES_DIRS

register = template.Library()


class ThemesList(template.Node):
    def render(self, context):
        themes = []
        for d in STATICFILES_DIRS:
            try:
                themes += os.listdir(os.path.join(d, 'css/themes'))
            except OSError:
                pass
        context['themes_list'] = themes
        return ''


@register.tag
def get_themes_list(parser, token):
    return ThemesList()

