# -*- coding: utf-8 -*-

from django.db import migrations


# noinspection PyUnusedLocal
def populate_config(apps, schema_editor):
    # noinspection PyPep8Naming
    Config = apps.get_model('main', 'Config')
    default_config = {
        'main_page': '-1',
        'title': 'Title Undefined',
    }
    for key in default_config:
        config = Config()
        config.key, config.value = key, default_config[key]
        config.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_config),
    ]
