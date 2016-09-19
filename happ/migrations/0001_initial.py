# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(verbose_name='Creation Date', null=True, blank=True)),
                ('browser', models.CharField(max_length=1000)),
                ('ip', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('companyname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(verbose_name='Creation Date', null=True, blank=True)),
                ('browser', models.CharField(max_length=1000)),
                ('ip', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('capture', models.FileField(verbose_name='Image', upload_to='captures/')),
                ('result', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(verbose_name='Creation Date', null=True, blank=True)),
                ('employee', models.ForeignKey(null=True, to='happ.Employee', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(verbose_name='Creation Date', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('image', models.FileField(verbose_name='Image', upload_to='exercises/')),
                ('creation_date', models.DateTimeField(verbose_name='Creation Date', null=True, blank=True)),
                ('employer', models.ForeignKey(null=True, to='happ.Employer', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('image', models.FileField(verbose_name='Image', upload_to='exercises/')),
                ('video', models.FileField(verbose_name='Image', null=True, blank=True, upload_to='motivations/')),
                ('creation_date', models.DateTimeField(verbose_name='Creation Date', null=True, blank=True)),
                ('employer', models.ForeignKey(null=True, to='happ.Employer', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField(verbose_name='Creation Date', null=True, blank=True)),
                ('employee', models.ManyToManyField(null=True, to='happ.Employee', blank=True)),
                ('employer', models.ForeignKey(null=True, to='happ.Employer', blank=True)),
                ('exercise', models.ManyToManyField(null=True, to='happ.Exercise', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Motivation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('image', models.FileField(verbose_name='Image', null=True, blank=True, upload_to='motivations/')),
                ('video', models.FileField(verbose_name='Image', null=True, blank=True, upload_to='motivations/')),
                ('creation_date', models.DateTimeField(verbose_name='Creation Date', null=True, blank=True)),
                ('employer', models.ForeignKey(null=True, to='happ.Employer', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(verbose_name='Creation Date', null=True, blank=True)),
                ('employer', models.ForeignKey(null=True, to='happ.Employer', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('icon', models.FileField(verbose_name='Image', upload_to='soundicons/')),
                ('sound', models.FileField(verbose_name='Sound', upload_to='sounds/')),
                ('color', models.CharField(max_length=20)),
                ('creation_date', models.DateTimeField(verbose_name='Creation Date', null=True, blank=True)),
                ('employer', models.ForeignKey(null=True, to='happ.Employer', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Taks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('creation_date', models.DateTimeField(verbose_name='Creation Date', null=True, blank=True)),
                ('due_date', models.DateTimeField(verbose_name='Due Date', null=True, blank=True)),
                ('employee', models.ForeignKey(null=True, to='happ.Employee', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task_Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(verbose_name='Creation Date', null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='taks',
            name='status',
            field=models.ForeignKey(null=True, to='happ.Task_Status', blank=True),
        ),
        migrations.AddField(
            model_name='message',
            name='motivation',
            field=models.ManyToManyField(null=True, to='happ.Motivation', blank=True),
        ),
        migrations.AddField(
            model_name='message',
            name='quote',
            field=models.ManyToManyField(null=True, to='happ.Quote', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='eventtype',
            field=models.ForeignKey(null=True, to='happ.Event_Type', blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='employer',
            field=models.ForeignKey(null=True, to='happ.Employer', blank=True),
        ),
    ]
