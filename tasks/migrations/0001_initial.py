# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-29 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('status', models.SmallIntegerField(choices=[(1, 'Waiting'), (2, 'In Progress'), (3, 'Code Review'), (4, 'Testing'), (5, 'Completed')], null=True)),
                ('order', models.SmallIntegerField(default=0)),
                ('due', models.DateField(blank=True, null=True)),
                ('started', models.DateTimeField(blank=True, null=True)),
                ('completed', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
