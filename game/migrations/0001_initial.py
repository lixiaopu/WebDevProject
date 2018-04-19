# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-21 18:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import game.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.URLField(unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=game.models.user_directory_path)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('available', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]