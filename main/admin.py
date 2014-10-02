from django.contrib import admin
from main.models import Config, StandardPage, MainMenu


class MainMenuAdmin(admin.ModelAdmin):
    fields = ['title', 'dest_page', 'dest_url']


class StandardPageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Content', {'fields': ['content'], 'classes': ['collapse']}),
    ]


class ConfigAdmin(admin.ModelAdmin):
    fields = ['key', 'value', ]


admin.site.register(MainMenu, MainMenuAdmin)
admin.site.register(StandardPage, StandardPageAdmin)
admin.site.register(Config, ConfigAdmin)
