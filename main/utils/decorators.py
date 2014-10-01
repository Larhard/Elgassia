import django.contrib.admin.views.decorators as admin
import django.contrib.auth.decorators as auth


def staff_member_required(redirect_field_name=None, login_url='main:home'):
    def wrapper(view_func):
        return admin.staff_member_required(view_func, redirect_field_name=redirect_field_name, login_url=login_url)
    return wrapper


def login_required(redirect_field_name=None, login_url='main:home'):
    def wrapper(view_func):
        return auth.login_required(view_func, redirect_field_name=redirect_field_name, login_url=login_url)
    return wrapper
