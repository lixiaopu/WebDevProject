# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-17 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_game_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='release_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='revenue',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='game',
            name='score_board',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='sold_qty',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
