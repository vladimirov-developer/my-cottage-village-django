# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-05 10:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_name', models.CharField(max_length=255, verbose_name='\u043e\u0442 \u043a\u043e\u0433\u043e')),
                ('text', models.TextField(verbose_name='\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435')),
                ('is_new', models.BooleanField(default=True, verbose_name='\u043d\u043e\u0432\u043e\u0435')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': '\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043d\u044b\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='MessageSender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_name', models.CharField(default='\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f', max_length=255, verbose_name='\u043e\u0442 \u043a\u043e\u0433\u043e')),
                ('text', models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('users', models.ManyToManyField(blank=True, help_text='\u041e\u0441\u0442\u0430\u0432\u0442\u0435 \u043f\u043e\u043b\u0435 \u043f\u0443\u0441\u0442\u044b\u043c, \u0435\u0441\u043b\u0438 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043e \u0441\u0440\u0430\u0437\u0443 \u0432\u0441\u0435\u043c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u043c.', to=settings.AUTH_USER_MODEL, verbose_name='\u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u0438')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': '\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f',
            },
        ),
    ]
