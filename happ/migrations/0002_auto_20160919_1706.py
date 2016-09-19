# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happ', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='browser',
            field=models.CharField(null=True, blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='employee',
            name='ip',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='employer',
            name='browser',
            field=models.CharField(null=True, blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='employer',
            name='ip',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='message',
            name='employee',
            field=models.ManyToManyField(to='happ.Employee'),
        ),
        migrations.AlterField(
            model_name='message',
            name='exercise',
            field=models.ManyToManyField(to='happ.Exercise'),
        ),
        migrations.AlterField(
            model_name='message',
            name='motivation',
            field=models.ManyToManyField(to='happ.Motivation'),
        ),
        migrations.AlterField(
            model_name='message',
            name='quote',
            field=models.ManyToManyField(to='happ.Quote'),
        ),
    ]
