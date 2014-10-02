from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from custom_auth.models import CustomUser


admin.site.register(CustomUser, UserAdmin)
