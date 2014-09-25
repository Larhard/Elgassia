from django.shortcuts import HttpResponse
from main.models import MainMenu, PopupMenu
import json


def save_main_menu(request):
    error = ''

    # TODO edit url's

    try:
        menu_db = MainMenu.objects
        idx = request.POST.getlist('idx[]')
        title = request.POST.getlist('title[]')
        dest_name = request.POST.getlist('dest_name[]')
        dest_url = request.POST.getlist('dest_url[]')

        for pos, entry in enumerate(zip(idx, title, dest_name, dest_url)):
            k = menu_db.get(id=entry[0])
            k.position = pos
            k.title, k.dest_name, k.dest_url = entry[1:]
            k.save()
    except Exception as e:
        error = e.message

    response = {'success': error == '', 'error': error}
    return HttpResponse(json.dumps(response), content_type='application/json')
