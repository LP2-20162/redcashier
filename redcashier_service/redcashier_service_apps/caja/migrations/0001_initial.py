# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-04 19:38
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modcontable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('contanual', models.CharField(max_length=50)),
                ('regisanual', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Modcontable',
                'permissions': (('list_modcontable', 'Can list modcontable'), ('get_modcontable', 'Can get modcontable')),
                'verbose_name_plural': 'Modcontables',
            },
        ),
        migrations.CreateModel(
            name='Usercashier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(blank=True, max_length=20, null=True)),
                ('usuario', models.CharField(max_length=20)),
                ('perfil', models.CharField(max_length=20)),
                ('sucursal', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Usercashier',
                'permissions': (('list_usercashier', 'Can list usercashier'), ('get_usercashier', 'Can get usercashier')),
                'verbose_name_plural': 'Usercashiers',
            },
        ),
    ]
