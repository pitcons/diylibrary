# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151203_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='returned_at',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
