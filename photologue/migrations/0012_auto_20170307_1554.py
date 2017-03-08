# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.html import strip_tags


def forward(apps, schema_editor):
    Photo = apps.get_model('photologue.Photo')
    for item in Photo.objects.all():
        item.alt_tag = strip_tags(item.caption).strip()[:200]
        item.save()


def backward(apps, schema_editor):
    Photo = apps.get_model('photologue.Photo')
    Photo.objects.update(alt_tag='')


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0011_auto_20170307_1552'),
    ]

    operations = [
        migrations.RunPython(forward, backward),
    ]
