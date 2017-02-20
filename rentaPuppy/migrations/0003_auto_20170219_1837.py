# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-20 02:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentaPuppy', '0002_dogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='dog_tricks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trick_name', models.CharField(max_length=250)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentaPuppy.dogs')),
            ],
        ),
        migrations.DeleteModel(
            name='Greeting',
        ),
    ]
