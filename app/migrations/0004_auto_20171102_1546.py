# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20171025_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=models.CharField(help_text='可选项, 若为空格则摘取正文前100个字符', max_length=100, null=True, verbose_name='文章摘要'),
        ),
    ]
