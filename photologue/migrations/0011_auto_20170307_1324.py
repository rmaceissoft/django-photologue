# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20150924_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='alt_tag',
            field=models.TextField(verbose_name='Alt Tag', blank=True),
            preserve_default=True,
        ),
    ]
