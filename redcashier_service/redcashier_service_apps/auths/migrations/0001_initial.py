# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-04 19:38
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import redcashier_service_apps.auths.models.user
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('last_hierarchy_id', models.CharField(blank=True, max_length=50, null=True)),
                ('last_module_id', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
                ('registered_by', models.TextField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'User',
                'permissions': (('list_user', 'Can list user'), ('get_user', 'Can get user')),
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', redcashier_service_apps.auths.models.user.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Hierarchy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('logo', models.ImageField(blank=True, default='logo/default.png', null=True, upload_to='logos', verbose_name='Logo')),
                ('code', models.CharField(blank=True, max_length=60, null=True, verbose_name='Code')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('name_short', models.CharField(blank=True, max_length=40, null=True, verbose_name='Name short')),
                ('fiscal_creation_date', models.DateField(blank=True, null=True, verbose_name='fiscal creation date')),
                ('fiscal_address', models.CharField(blank=True, max_length=40, null=True, verbose_name='Fiscal address')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
                ('registered_by', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'hierarchy',
                'permissions': (('list_hierarchy', 'Can list hierarchy'), ('get_hierarchy', 'Can get hierarchy')),
                'verbose_name_plural': 'hierarchys',
            },
        ),
        migrations.CreateModel(
            name='HierarchyType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hierarchy_type', models.CharField(choices=[('INSTITUCION', 'Institucion'), ('FILIAL', 'Filial'), ('FACULTAD', 'Facultad'), ('ESCUELA', 'Escuela'), ('CARRERA', 'Carrera'), ('DEPARTAMENTO_ACAD', 'Departamento acad.'), ('OTHER', 'Other')], max_length=50)),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('level', models.BigIntegerField(verbose_name='Level')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
                ('registered_by', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'hierarchy type',
                'permissions': (('list_hierarchytype', 'Can list hierarchytype'), ('get_hierarchytype', 'Can get hierarchytype')),
                'db_table': 'auths_hierarchy_type',
                'verbose_name_plural': 'hierarchy types',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('module', models.CharField(choices=[('WEB', 'Web informativa'), ('ADMISION', 'Admisión'), ('BACKEND', 'Backend Manager'), ('OTHER', 'Other')], default='BACKEND', max_length=50, verbose_name='module')),
                ('state', models.CharField(help_text='state or section (estado o grupo de estados)', max_length=50, verbose_name='State or section')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('url', models.CharField(default='#', max_length=150, verbose_name='Url')),
                ('template_url', models.CharField(default='#', max_length=250, verbose_name='Template url')),
                ('pos', models.IntegerField(default=1, verbose_name='position')),
                ('icon', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='icon')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_abstract', models.BooleanField(default=False, verbose_name='Is_abstract')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('router_json', models.TextField(blank=True, null=True, verbose_name='router json')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
                ('registered_by', models.TextField(blank=True, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='auths.Menu', verbose_name='parent')),
                ('permission', models.ForeignKey(blank=True, help_text='NULL if is root', null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Permission', verbose_name='permission')),
            ],
            options={
                'verbose_name': 'menu',
                'permissions': (('list_menu', 'Can list menu'), ('get_menu', 'Can get menu')),
                'verbose_name_plural': 'menus',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('national_id_doc', models.CharField(blank=True, max_length=20, null=True, verbose_name='National identity document')),
                ('first_name', models.CharField(help_text='primer nombre', max_length=50, verbose_name='First name')),
                ('other_names', models.CharField(blank=True, help_text='otros nombres', max_length=50, null=True, verbose_name='Other names')),
                ('last_name', models.CharField(blank=True, help_text='apellido paterno', max_length=50, null=True, verbose_name='Last name')),
                ('mother_last_name', models.CharField(blank=True, help_text='apellido materno', max_length=50, null=True, verbose_name="Mother's last name")),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='birth date')),
                ('photo', models.ImageField(blank=True, default='persons/default.png', null=True, upload_to='persons', verbose_name='Photo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
                ('registered_by', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
        migrations.CreateModel(
            name='UserHierarchyGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('access_info', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='start date')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='end date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
                ('registered_by', models.TextField(blank=True, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='group')),
                ('hierarchy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auths.Hierarchy', verbose_name='hierarchy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'user hierarchy group',
                'db_table': 'auths_user_hierarchy_group',
                'verbose_name_plural': 'user hierarchy group',
            },
        ),
        migrations.CreateModel(
            name='UserHierarchyPermission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('access_info', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='start date')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='end date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
                ('registered_by', models.TextField(blank=True, null=True)),
                ('hierarchy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auths.Hierarchy', verbose_name='hierarchy')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Permission', verbose_name='permission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'user hierarchy permission',
                'db_table': 'auths_user_hierarchy_permission',
                'verbose_name_plural': 'user hierarchy permission',
            },
        ),
        migrations.AddField(
            model_name='hierarchy',
            name='hierarchy_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hierarchy_set', to='auths.HierarchyType'),
        ),
        migrations.AddField(
            model_name='hierarchy',
            name='immediate_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='immediate_childrens', to='auths.Hierarchy'),
        ),
        migrations.AddField(
            model_name='hierarchy',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='auths.Hierarchy'),
        ),
        migrations.AddField(
            model_name='user',
            name='person',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auths.Person', verbose_name='Person'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
