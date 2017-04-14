# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 07:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_django', '0006_partial'),
        ('shareWear', '0016_auto_20170409_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='social_media_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='shareWear.profile')),
                ('social_media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_media', to='social_django.UserSocialAuth')),
            ],
        ),
    ]
