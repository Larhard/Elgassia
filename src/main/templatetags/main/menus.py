from django import template

import main.models

register = template.Library()


class PopupMenuNode(template.Node):
    def render(self, context):
        context['popup_menu'] = main.models.PopupMenu.objects.all()
        return ''


@register.tag()
def get_popup_menu(parser, token):
    return PopupMenuNode()


class MainMenuNode(template.Node):
    def render(self, context):
        context['main_menu'] = main.models.MainMenu.objects.all()
        return ''


@register.tag()
def get_main_menu(parser, token):
    return MainMenuNode()
