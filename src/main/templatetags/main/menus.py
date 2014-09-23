from django import template

register = template.Library()


class PopupMenuNode(template.Node):  # TODO connect with model
    def render(self, context):
        context['popup_menu'] = ['Language', 'Skin', 'login, password']
        return ''


@register.tag()
def get_popup_menu(parser, token):
    return PopupMenuNode()


class MainMenuNode(template.Node):  # TODO connect with model
    def render(self, context):
        context['main_menu'] = ['New Home', 'New Link 1', 'New Link 2']
        return ''


@register.tag()
def get_main_menu(parser, token):
    return MainMenuNode()
