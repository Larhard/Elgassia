import json

from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie

from main.models import StandardPage, Config
from main.utils.decorators import login_required


@ensure_csrf_cookie
def home(request):
    try:
        return page_view(request, Config.objects.get(key='main_page').value)
    except ObjectDoesNotExist:
        return page_view(request, -1)


def login_view(request):
    error = ''

    username = request.POST['login']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        error += 'login or password incorrect'

    response = {'success': error == '', 'error': error}
    return HttpResponse(json.dumps(response), content_type='application/json')


def logout_view(request):
    error = ''

    logout(request)

    response = {'success': error == '', 'error': error}
    return HttpResponse(json.dumps(response), content_type='application/json')


def page_view(request, idx):
    try:
        page = StandardPage.objects.get(id=idx)
        return render(request, 'main/page.html', {
            'page': page,
        })
    except ObjectDoesNotExist:
        return render(request, 'main/page_not_found.html')


def change_theme(request):
    error = ''

    new_theme = request.POST['new_theme']

    response = {'success': error == '', 'error': error}
    result = HttpResponse(json.dumps(response), content_type='application/json')
    result.set_cookie('theme', new_theme)
    return result


@login_required()
def account_edit(request):
    return render(request, 'main/account_edit.html')


@login_required()
def account_save(request):
    error = ''

    email = request.POST['email']
    password = request.POST['password']

    request.user.set_email(email)
    if password:
        request.user.set_password(password)

    request.user.save()

    response = {'success': error == '', 'error': error}
    result = HttpResponse(json.dumps(response), content_type='application/json')
    return result
