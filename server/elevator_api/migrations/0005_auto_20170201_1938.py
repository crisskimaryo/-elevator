# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elevator_api', '0004_auto_20170201_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='model',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='owner',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='plateno',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='ownermodel',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ownermodel',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='elevator_api.carmodel'),
        ),
        migrations.AddField(
            model_name='ownermodel',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ownermodel',
            name='fname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ownermodel',
            name='gender',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ownermodel',
            name='idno',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ownermodel',
            name='idtype',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ownermodel',
            name='lname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ownermodel',
            name='mobile',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
