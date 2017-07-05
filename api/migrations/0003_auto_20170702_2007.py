# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 00:07
from __future__ import unicode_literals

import api.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170702_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParameterImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', validators=[api.validators.validate_image_extension])),
            ],
        ),
        migrations.RemoveField(
            model_name='parameters',
            name='image',
        ),
        migrations.AddField(
            model_name='parameterimage',
            name='parameters',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.Parameters'),
        ),
    ]