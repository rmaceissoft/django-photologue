# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def forwards(apps, schema_editor):
    """
    sql = schema_editor.sql_create_column % {
        'table':'photologue_gallery_photos',
        'column': 'sort_value',
        'definition': 'integer NOT NULL DEFAULT 0'
    }
    schema_editor.execute(sql)
    """
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0009_auto_20150924_1322'),
    ]

    operations = [
        migrations.RunPython(forwards)
    ]
