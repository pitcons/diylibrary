# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20160110_2219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['name'], 'verbose_name': '\u0430\u0432\u0442\u043e\u0440', 'verbose_name_plural': '\u0430\u0432\u0442\u043e\u0440\u044b'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title'], 'verbose_name': '\u043a\u043d\u0438\u0433\u0430', 'verbose_name_plural': '\u043a\u043d\u0438\u0433\u0438'},
        ),
        migrations.AlterModelOptions(
            name='owner',
            options={'ordering': ['name'], 'verbose_name': '\u0432\u043b\u0430\u0434\u0435\u043b\u0435\u0446', 'verbose_name_plural': '\u0432\u043b\u0430\u0434\u0435\u043b\u044c\u0446\u044b'},
        ),
        migrations.AlterModelOptions(
            name='reader',
            options={'ordering': ['name'], 'verbose_name': '\u0447\u0438\u0442\u0430\u0442\u0435\u043b\u044c', 'verbose_name_plural': '\u0447\u0438\u0442\u0430\u0442\u0435\u043b\u0438'},
        ),
        migrations.AlterModelOptions(
            name='reading',
            options={'ordering': ['took_at'], 'verbose_name': '\u0432\u0437\u044f\u0442\u0430\u044f \u043a\u043d\u0438\u0433\u0430', 'verbose_name_plural': '\u0432\u0437\u044f\u0442\u044b\u0435 \u043a\u043d\u0438\u0433\u0438'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['name'], 'verbose_name': '\u0440\u0430\u0437\u0434\u0435\u043b', 'verbose_name_plural': '\u0440\u0430\u0437\u0434\u0435\u043b\u044b'},
        ),
        migrations.AlterField(
            model_name='reading',
            name='returned_at',
            field=models.DateField(default=None, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0435\u043d\u0438\u044f', db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='reading',
            name='took_at',
            field=models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0432\u0437\u044f\u0442\u0438\u044f', db_index=True),
        ),
    ]
