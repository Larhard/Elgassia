from django.contrib.auth.decorators import user_passes_test


def staff_member_required(view_func, redirect_field_name=None, login_url='main:home'):
    return user_passes_test(
        lambda u: u.is_active and u.is_staff,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )(view_func)
