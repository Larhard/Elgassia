from django.shortcuts import render
from django.shortcuts import render_to_response


def home(request):
    return render_to_response('main/home.html')


def login(request):
    return render_to_response('main/home.html')
