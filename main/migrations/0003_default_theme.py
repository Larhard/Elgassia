# -*- coding: utf-8 -*-

from django.db import migrations


# noinspection PyUnusedLocal
def populate_config(apps, schema_editor):
    # noinspection PyPep8Naming
    Config = apps.get_model('main', 'Config')
    default_config = {
        'default_theme': 'dark',
    }
    for key in default_config:
        config, created = Config.objects.get_or_create(key=key, defaults={'value': default_config[key]})


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0002_populate_config'),
    ]

    operations = [
        migrations.RunPython(populate_config),
    ]
