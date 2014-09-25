from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from main.models import StandardPage, Config


@ensure_csrf_cookie
def home(request):
    return page_view(request, Config.objects.get(key='main_page').value)


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