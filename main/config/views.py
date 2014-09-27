import json
from django.core.urlresolvers import reverse

from django.db.utils import IntegrityError
from django.shortcuts import HttpResponse, render

from elgassia.settings import DEBUG
from main.models import MainMenu, StandardPage, Config
from main.utils.decorators import staff_member_required


@staff_member_required
def save_main_menu(request):
    error = ''

    try:
        menu_db = MainMenu.objects
        idx = request.POST.getlist('idx[]')
        title = request.POST.getlist('title[]')
        dest_page = request.POST.getlist('dest_page[]')
        dest_url = request.POST.getlist('dest_url[]')
        remove = request.POST.getlist('remove[]')

        for pos, entry in enumerate(zip(idx, remove, title, dest_page, dest_url)):
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
            k.title, k.dest_page, k.dest_url = entry[2:]
            k.save()
    except Exception as e:
        if DEBUG:
            error += str(e)
        else:
            error += 'Saving Error'

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

    for entry in zip(idx, remove, title):
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

    next_page = request.GET.get('next', '')
    next_page = next_page or reverse('main:home')

    return render(request, 'main/config/page_edit.html', {'page': page, 'next_page': next_page})


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


@staff_member_required
def config_editor(request):
    configs = Config.objects.all()
    return render(request, 'main/config/config_editor.html', {
        'configs': configs
    })


@staff_member_required
def config_editor_save(request):
    error = ''

    try:
        idx = request.POST.getlist('idx[]')
        remove = request.POST.getlist('remove[]')
        key = request.POST.getlist('key[]')
        value = request.POST.getlist('value[]')

        for entry in zip(idx, remove, key, value):
            if entry[0] == "-1":
                if entry[1] == 'true':
                    continue
                k = Config()
            else:
                k = Config.objects.get(id=entry[0])
                if entry[1] == 'true':
                    k.delete()
                    continue
            k.key, k.value = entry[2:]
            k.save()
    except IntegrityError as e:
        error += e.message

    response = {'success': error == '', 'error': error}
    return HttpResponse(json.dumps(response), content_type='application/json')
