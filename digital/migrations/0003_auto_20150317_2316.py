# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0002_auto_20150317_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='available_text',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
