from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def home(request):
    return render_to_response('main/home.html')


def login(request):
    return render_to_response('main/home.html')
