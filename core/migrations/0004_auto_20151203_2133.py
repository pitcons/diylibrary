# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151111_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('took_at', models.DateField()),
                ('returned_at', models.CharField(max_length=64)),
                ('book', models.ForeignKey(to='core.Book')),
                ('reader', models.ForeignKey(to='core.Reader')),
            ],
        ),
        migrations.AddField(
            model_name='reader',
            name='books',
            field=models.ManyToManyField(to='core.Book', through='core.Reading'),
        ),
    ]
