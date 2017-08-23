# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-24 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('Number', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='编号')),
                ('Bookname', models.CharField(max_length=30, verbose_name='书名')),
                ('Press', models.CharField(max_length=30, verbose_name='出版社')),
                ('Author', models.CharField(max_length=30, verbose_name='作者')),
                ('Edition', models.CharField(max_length=10, verbose_name='版次')),
                ('Price', models.FloatField(max_length=30, verbose_name='单价')),
            ],
            options={
                'verbose_name': '书籍信息表',
                'verbose_name_plural': '书籍信息表',
                'db_table': 'bookinfor',
            },
        ),
        migrations.CreateModel(
            name='BookOrder',
            fields=[
                ('Number', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='编号')),
                ('CourseID', models.IntegerField(max_length=10)),
                ('Amount', models.IntegerField(max_length=10)),
                ('Term', models.CharField(max_length=30)),
                ('Major', models.CharField(max_length=30)),
            ],
        ),
    ]
