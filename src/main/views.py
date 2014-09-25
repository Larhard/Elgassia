from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie
import json


@ensure_csrf_cookie
def home(request):
    return render_to_response('main/home.html')


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
