# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20160106_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='reader',
            name='email',
            field=models.CharField(max_length=64, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0439 \u043f\u043e\u0447\u0442\u044b', blank=True),
        ),
        migrations.AddField(
            model_name='reader',
            name='phone',
            field=models.CharField(max_length=64, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', blank=True),
        ),
    ]
