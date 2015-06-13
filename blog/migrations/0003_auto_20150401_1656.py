# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150331_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_leaf',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='is_root',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
