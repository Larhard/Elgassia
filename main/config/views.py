import json
from django.contrib.auth import get_user_model

from django.core.urlresolvers import reverse
from django.db.utils import IntegrityError
from django.shortcuts import HttpResponse, render
from django.shortcuts import render_to_response

from elgassia.settings import DEBUG
from main.models import MainMenu, StandardPage, Config
from main.utils.decorators import staff_member_required


@staff_member_required()
def main_menu_save(request):
    error = ''

    try:
        menu_db = MainMenu.objects
        idx = request.POST.getlist('idx[]')
        title = request.POST.getlist('title[]')
        dest_page = request.POST.getlist('dest_page[]')
        dest_url = request.POST.getlist('dest_url[]')
        remove = request.POST.getlist('remove[]')

        for pos, entry in enumerate(zip(idx, remove, title, dest_page, dest_url)):
            if entry[0] == '-1':
                if entry[1] == 'true':
                    continue
                k = MainMenu()
            else:
                k = menu_db.get(id=entry[0])
                if entry[1] == 'true':
                    k.delete()
                    continue
            k.position = pos

            if entry[3] == 'new':
                dest_page = StandardPage()
                dest_page.title = entry[2]
                dest_page.save()
                entry = list(entry)
                entry[3] = dest_page.id

            k.title, k.dest_page, k.dest_url = entry[2:]
            k.save()
    except Exception as e:
        if DEBUG:
            error += str(e)
        else:
            error += 'Saving Error'

    response = {'success': error == '', 'error': error}
    return HttpResponse(json.dumps(response), content_type='application/json')


@staff_member_required()
def page_list(request):
    return render(request, 'main/config/page_list.html', {
        'pages': StandardPage.objects.all()
    })


@staff_member_required()
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


@staff_member_required()
def page_edit(request, idx):
    page = StandardPage.objects.get(id=idx)

    next_page = request.GET.get('next', '')
    next_page = next_page or reverse('main:home')

    return render(request, 'main/config/page_edit.html', {'page': page, 'next_page': next_page})


@staff_member_required()
def page_edit_save(request):
    error = ''
    try:
        idx = request.POST['idx']
        content = request.POST['content']
        title = request.POST['title']
        page = StandardPage.objects.get(id=idx)
        page.content = content
        page.title = title
        page.save()
    except Exception as e:
        error += e.message
    response = {'success': error == '', 'error': error}
    return HttpResponse(json.dumps(response), content_type='application/json')


@staff_member_required()
def config_editor(request):
    configs = Config.objects.all()
    return render(request, 'main/config/config_editor.html', {
        'configs': configs
    })


@staff_member_required()
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


@staff_member_required()
def user_list_view(request):
    User = get_user_model()
    return render(request, 'main/config/user_list.html', {
        'users': User.objects.all()
    })


@staff_member_required()
def user_save(request):
    error = ''
    response = {
        'removed': False,
        'idx': None,
    }

    try:
        idx = request.POST['idx']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        remove = request.POST['remove']

        User = get_user_model()
        try:
            user = None
            if idx == '-1':
                if remove != 'true':
                    user_data = {'username': username, 'email': email}
                    if password:
                        user_data['password'] = password
                    user = User.objects.create_user(**user_data)
            else:
                user = User.objects.get(id=idx)
                if remove == 'true':
                    user.delete()
                    response['removed'] = True
                else:
                    user.username = username
                    user.set_email(email)
                    if password:
                        user.set_password(password)
                    user.save()
            response['idx'] = user.id
        except (IntegrityError, ValueError, ) as e:
            error += e.message
    except Exception as e:
        print e.message
        print type(e)

    response['success'] = error == ''
    response['error'] = error
    return HttpResponse(json.dumps(response), content_type='application/json')
