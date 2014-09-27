# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20140926_0019'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PopupMenu',
        ),
        migrations.RemoveField(
            model_name='menugeneric',
            name='dest_name',
        ),
    ]
