from django.shortcuts import HttpResponse
from main.models import MainMenu, PopupMenu
import json


def save_main_menu(request):
    error = ''

    try:
        menu_db = MainMenu.objects
        idx = request.POST.getlist('idx[]')
        title = request.POST.getlist('title[]')
        dest_name = request.POST.getlist('dest_name[]')
        dest_url = request.POST.getlist('dest_url[]')
        remove = request.POST.getlist('remove[]')

        for pos, entry in enumerate(zip(idx, remove, title, dest_name, dest_url)):
            if entry[0] == "-1":
                if entry[1] == 'true':
                    continue
                k = MainMenu()
            else:
                k = menu_db.get(id=entry[0])
                if entry[1] == 'true':
                    k.delete()
                    continue
            k.position = pos
            k.title, k.dest_name, k.dest_url = entry[2:]
            k.save()
    except Exception as e:
        error = e.message

    response = {'success': error == '', 'error': error}
    return HttpResponse(json.dumps(response), content_type='application/json')
