# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0012_auto_20170307_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='alt_tag',
            field=models.CharField(help_text='\n            <p style="font-weight: 900;">Keep it simple</p>\n            <p>Master the art of saying a lot with a little.</p>\n            <p style="font-weight: 900;">Be descriptive yet succinct</p>\n            <p>Be strategic with your descriptions.</p>\n            <p style="font-weight: 900;">Consider the text surrounding the image</p>\n            <p>Placing images with alt tags near relevant text will help create a coherent\n            experience for non-visual users</p>\n            <p style="font-weight: 900;">Utilize keywords to help your site rank better in search</p>\n            <p>It\'s a great strategy to use your site\'s keywords in order to help your images rank</p>\n            <p>Be careful not to misuse your keywords as it could end up hurting your SEO instead of helping</p>\n        ', max_length=200),
            preserve_default=True,
        ),
    ]
