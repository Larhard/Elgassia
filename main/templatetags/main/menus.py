from django import template

from main.models import MainMenu, PopupMenu

register = template.Library()


class PopupMenuNode(template.Node):
    def render(self, context):
        context['popup_menu'] = PopupMenu.objects.order_by('position')
        return ''


@register.tag()
def get_popup_menu(parser, token):
    return PopupMenuNode()


class MainMenuNode(template.Node):
    def render(self, context):
        context['main_menu'] = MainMenu.objects.order_by('position')
        return ''


@register.tag()
def get_main_menu(parser, token):
    return MainMenuNode()

