# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuGeneric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('dest_url', models.CharField(max_length=256)),
                ('dest_name', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('menugeneric_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='main.MenuGeneric')),
            ],
            options={
            },
            bases=('main.menugeneric',),
        ),
        migrations.CreateModel(
            name='PopupMenu',
            fields=[
                ('menugeneric_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='main.MenuGeneric')),
            ],
            options={
            },
            bases=('main.menugeneric',),
        ),
    ]
