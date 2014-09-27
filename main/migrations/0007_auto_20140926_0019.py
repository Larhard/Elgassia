# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_populate_config'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='key',
            field=models.CharField(unique=True, max_length=256),
        ),
    ]
