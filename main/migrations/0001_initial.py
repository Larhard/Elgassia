# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


# noinspection PyUnresolvedReferences
class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=256)),
                ('value', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuGeneric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=256)),
                ('dest_url', models.CharField(default=b'', max_length=256)),
                ('dest_page', models.CharField(default=b'', max_length=256)),
                ('position', models.IntegerField(default=2147483647)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('menugeneric_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False,
                                      to='main.MenuGeneric')),
            ],
            options={
            },
            bases=('main.menugeneric',),
        ),
        migrations.CreateModel(
            name='PageGeneric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StandardPage',
            fields=[
                ('pagegeneric_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False,
                                      to='main.PageGeneric')),
            ],
            options={
            },
            bases=('main.pagegeneric',),
        ),
    ]
