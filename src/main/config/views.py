import json

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import HttpResponse, render
from django.shortcuts import render_to_response

from main.models import MainMenu, StandardPage


@staff_member_required
def save_main_menu(request):
    error = ''

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

    response = {'success': error == '', 'error': error}
    return HttpResponse(json.dumps(response), content_type='application/json')


@staff_member_required
def page_list(request):
    return render(request, 'main/config/page_list.html', {
        'pages': StandardPage.objects.all()
    })


@staff_member_required
def page_list_save(request):
    error = ''

    idx = request.POST.getlist('idx[]')
    title = request.POST.getlist('title[]')
    remove = request.POST.getlist('remove[]')

    for pos, entry in enumerate(zip(idx, remove, title)):
        if entry[0] == '-1':
            if entry[1] == 'true':
                continue
            k = StandardPage()
        else:
            k = StandardPage.objects.get(id=entry[0])
            if entry[1] == 'true':
                k.delete()
                continue
        k.title = entry[2]
        k.save()

    response = {'success': error == '', 'error': error}
    return HttpResponse(json.dumps(response), content_type='application/json')


@staff_member_required
def page_edit(request, idx):
    page = StandardPage.objects.get(id=idx)
    return render(request, 'main/config/page_edit.html', {'page': page})


@staff_member_required
def page_edit_save(request):
    error = ''
    try:
        idx = request.POST['idx']
        content = request.POST['content']
        page = StandardPage.objects.get(id=idx)
        page.content = content
        page.save()
    except Exception as e:
        error += e.message
    response = {'success': error == '', 'error': error}
    return HttpResponse(json.dumps(response), content_type='application/json')
