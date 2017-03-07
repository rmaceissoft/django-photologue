# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.db.models import F


def forward(apps, schema_editor):
    Photo = apps.get_model('photologue.Photo')
    Photo.objects.update(alt_tag=F('caption'))


def backward(apps, schema_editor):
    Photo = apps.get_model('photologue.Photo')
    Photo.objects.update(alt_tag='')


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0011_auto_20170307_1324'),
    ]

    operations = [
        migrations.RunPython(forward, backward),
    ]
