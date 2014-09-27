from django import template

from main.models import StandardPage


register = template.Library()


class PageList(template.Node):
    def render(self, context):
        context['page_list'] = StandardPage.objects.order_by('title')
        return ''


# noinspection PyUnusedLocal
@register.tag
def get_page_list(parser, token):
    return PageList()
