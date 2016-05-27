# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-27 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('middlename', models.CharField(max_length=50)),
                ('dait_of_birth', models.DateField()),
                ('students_ticket', models.IntegerField(default=0)),
            ],
        ),
    ]
