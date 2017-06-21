# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='COGS',
            fields=[
                ('ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('OrgDetail', models.CharField(blank=True, max_length=256)),
                ('FinanceOwner', models.CharField(blank=True, max_length=256)),
                ('QTDAct', models.IntegerField(blank=True)),
                ('QTDFcst', models.IntegerField(blank=True)),
                ('QTDVTF', models.IntegerField(blank=True)),
                ('YTDAct', models.IntegerField(blank=True)),
                ('YTDBud', models.IntegerField(blank=True)),
                ('YTDVTB', models.IntegerField(blank=True)),
                ('CurrentQtrOutlook', models.IntegerField(blank=True)),
                ('ExecCommentary', models.TextField(blank=True)),
                ('CloseCommentary', models.TextField(blank=True)),
                ('ROCommentary', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OPEX',
            fields=[
                ('ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('OrgDetail', models.CharField(blank=True, max_length=256)),
                ('FinanceOwner', models.CharField(blank=True, max_length=256)),
                ('QTDAct', models.IntegerField(blank=True)),
                ('QTDFcst', models.IntegerField(blank=True)),
                ('QTDVTF', models.IntegerField(blank=True)),
                ('YTDAct', models.IntegerField(blank=True)),
                ('YTDBud', models.IntegerField(blank=True)),
                ('YTDVTB', models.IntegerField(blank=True)),
                ('CurrentQtrOutlook', models.IntegerField(blank=True)),
                ('ExecCommentary', models.TextField(blank=True)),
                ('CloseCommentary', models.TextField(blank=True)),
                ('ROCommentary', models.TextField(blank=True)),
            ],
        ),
    ]
