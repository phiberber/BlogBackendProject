# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-06-17 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloggerinfo',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='name_en',
        ),
        migrations.AddField(
            model_name='bloggerinfo',
            name='en_desc',
            field=models.CharField(default='', help_text='简介', max_length=300, verbose_name='简介'),
        ),
        migrations.AddField(
            model_name='bloggerinfo',
            name='en_name',
            field=models.CharField(blank=True, help_text='名称英文', max_length=20, null=True, verbose_name='名称英文'),
        ),
        migrations.AddField(
            model_name='navigationlink',
            name='en_desc',
            field=models.CharField(blank=True, help_text='英文简介', max_length=100, null=True, verbose_name='英文简介'),
        ),
        migrations.AddField(
            model_name='navigationlink',
            name='en_name',
            field=models.CharField(blank=True, help_text='英文名称', max_length=30, null=True, verbose_name='英文名称'),
        ),
        migrations.AddField(
            model_name='siteinfo',
            name='en_desc',
            field=models.CharField(blank=True, help_text='简介', max_length=150, null=True, verbose_name='简介'),
        ),
        migrations.AddField(
            model_name='siteinfo',
            name='en_name',
            field=models.CharField(blank=True, help_text='名称英文', max_length=20, null=True, verbose_name='名称英文'),
        ),
    ]