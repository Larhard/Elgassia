# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_pagegeneric_standardpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='menugeneric',
            name='dest_page',
            field=models.CharField(default=b'', max_length=256),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='menugeneric',
            name='dest_name',
            field=models.CharField(default=b'', max_length=256),
        ),
        migrations.AlterField(
            model_name='menugeneric',
            name='dest_url',
            field=models.CharField(default=b'', max_length=256),
        ),
        migrations.AlterField(
            model_name='menugeneric',
            name='title',
            field=models.CharField(default=b'', max_length=256),
        ),
    ]
