# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def init_slugs(apps, schema_editor):
    Gallery = apps.get_model('photologue', 'Gallery')
    Photo = apps.get_model('photologue', 'Photo')
    for item in Gallery.objects.all():
        item.slug = item.title_slug
        item.save()
    for item in Photo.objects.all():
        item.slug = item.title_slug
        item.save()


def dummy_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0007_auto_20150923_2132'),
    ]

    operations = [
        migrations.RunPython(init_slugs, reverse_code=dummy_reverse),
    ]
