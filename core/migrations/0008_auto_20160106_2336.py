# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tagging_autocomplete.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20160106_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=tagging_autocomplete.models.TagAutocompleteField(max_length=255, verbose_name='\u0422\u0435\u0433\u0438', blank=True),
        ),
    ]
