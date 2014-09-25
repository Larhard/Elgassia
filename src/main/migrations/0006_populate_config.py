# -*- coding: utf-8 -*-

from django.db import migrations


def populate_config(apps, schema_editor):
    Config = apps.get_model('main', 'Config')
    default_config = {
        'main_page': '1',
        'title': 'Title Undefined',
    }
    for key in default_config:
        config = Config()
        config.key, config.value = key, default_config[key]
        config.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_config'),
    ]

    operations = [
        migrations.RunPython(populate_config),
    ]
