# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tagging_autocomplete.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151220_2313'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '\u0430\u0432\u0442\u043e\u0440', 'verbose_name_plural': '\u0430\u0432\u0442\u043e\u0440\u044b'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '\u043a\u043d\u0438\u0433\u0430', 'verbose_name_plural': '\u043a\u043d\u0438\u0433\u0438'},
        ),
        migrations.AlterModelOptions(
            name='reader',
            options={'verbose_name': '\u0447\u0438\u0442\u0430\u0442\u0435\u043b\u044c', 'verbose_name_plural': '\u0447\u0438\u0442\u0430\u0442\u0435\u043b\u0438'},
        ),
        migrations.AlterModelOptions(
            name='reading',
            options={'verbose_name': '\u0432\u0437\u044f\u0442\u0430\u044f \u043a\u043d\u0438\u0433\u0430', 'verbose_name_plural': '\u0432\u0437\u044f\u0442\u044b\u0435 \u043a\u043d\u0438\u0433\u0438'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': '\u0440\u0430\u0437\u0434\u0435\u043b', 'verbose_name_plural': '\u0440\u0430\u0437\u0434\u0435\u043b\u044b'},
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=tagging_autocomplete.models.TagAutocompleteField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u0438\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='core.Author', verbose_name='\u0430\u0432\u0442\u043e\u0440\u044b'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=255, null=True, verbose_name='ISBN', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e (\u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e)'),
        ),
        migrations.AlterField(
            model_name='book',
            name='quantity_total',
            field=models.IntegerField(default=1, verbose_name='\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e (\u0432\u0441\u0435\u0433\u043e)'),
        ),
        migrations.AlterField(
            model_name='book',
            name='section',
            field=models.ForeignKey(verbose_name='\u0441\u0435\u043a\u0446\u0438\u044f', to='core.Section'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=512, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(null=True, verbose_name='\u0433\u043e\u0434', blank=True),
        ),
        migrations.AlterField(
            model_name='reader',
            name='books',
            field=models.ManyToManyField(to='core.Book', verbose_name='\u043a\u043d\u0438\u0433\u0438', through='core.Reading'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='name',
            field=models.CharField(max_length=512, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='book',
            field=models.ForeignKey(verbose_name='\u043a\u043d\u0438\u0433\u0430', to='core.Book'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='reader',
            field=models.ForeignKey(verbose_name='\u0447\u0438\u0442\u0430\u0442\u0435\u043b\u044c', to='core.Reader'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='returned_at',
            field=models.DateField(default=None, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0435\u043d\u0438\u044f', blank=True),
        ),
        migrations.AlterField(
            model_name='reading',
            name='took_at',
            field=models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0432\u0437\u044f\u0442\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
    ]
