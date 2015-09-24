# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('photologue', '0008_auto_20150923_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='sites',
            field=models.ManyToManyField(to='sites.Site', null=True, verbose_name='sites', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='sites',
            field=models.ManyToManyField(to='sites.Site', null=True, verbose_name='sites', blank=True),
            preserve_default=True,
        ),
    ]
