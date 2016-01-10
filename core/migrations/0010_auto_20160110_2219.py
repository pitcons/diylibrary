# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20160110_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512, verbose_name='\u0418\u043c\u044f')),
            ],
            options={
                'verbose_name': '\u0432\u043b\u0430\u0434\u0435\u043b\u0435\u0446',
                'verbose_name_plural': '\u0432\u043b\u0430\u0434\u0435\u043b\u044c\u0446\u044b',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='room_only',
            field=models.BooleanField(default=False, verbose_name='\u0422\u043e\u043b\u044c\u043a\u043e \u0447\u0438\u0442\u0430\u043b\u044c\u043d\u044b\u0439 \u0437\u0430\u043b'),
        ),
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(verbose_name='\u0432\u043b\u0430\u0434\u0435\u043b\u0435\u0446', blank=True, to='core.Owner', null=True),
        ),
    ]
