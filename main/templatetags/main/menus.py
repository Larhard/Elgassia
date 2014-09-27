from django import template

from main.models import MainMenu

register = template.Library()


class MainMenuNode(template.Node):
    def render(self, context):
        context['main_menu'] = MainMenu.objects.order_by('position')
        return ''


@register.tag()
def get_main_menu(parser, token):
    return MainMenuNode()

