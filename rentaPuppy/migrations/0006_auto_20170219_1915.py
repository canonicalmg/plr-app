# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-20 03:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentaPuppy', '0005_auto_20170219_1904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dog_pictures',
            old_name='img_src',
            new_name='image_src',
        ),
    ]
