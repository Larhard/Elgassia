from django.shortcuts import HttpResponse
from main.models import MainMenu, PopupMenu
import json


def save_main_menu(request):
    menu_entries = MainMenu.objects
    tmp = request.POST.keys()
    menu_order = request.POST.getlist('menu_order[]')
    for pos, idx in enumerate(menu_order):
        k = menu_entries.get(id=idx)
        k.position = pos
        k.save()

    response = {'success': True}
    return HttpResponse(json.dumps(response), content_type='application/json')
