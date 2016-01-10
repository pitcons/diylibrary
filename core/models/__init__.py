# -*- coding: utf-8 -*-
# http://www.isbnsearch.org/
from django.utils.translation import ugettext as _
from django.db import models
from tagging.fields import TagField
from tagging.registry import register
from tagging_autocomplete.models import TagAutocompleteField


class Author(models.Model):
    name = models.CharField(_(u'имя'), max_length=255)

    class Meta:
        verbose_name = _(u"автор")
        verbose_name_plural = _(u"авторы")
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(_(u'название'), max_length=255)

    class Meta:
        verbose_name = _(u"раздел")
        verbose_name_plural = _(u"разделы")
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Owner(models.Model):
    name = models.CharField(_(u'Имя'), max_length=512)

    class Meta:
        verbose_name = _(u"владелец")
        verbose_name_plural = _(u"владельцы")
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Book(models.Model):
    isbn = models.CharField(_(u'ISBN'), max_length=255, null=True, blank=True)
    title = models.CharField(_(u'название'), max_length=512)
    year = models.IntegerField(u'год', null=True, blank=True)
    quantity_total = models.IntegerField(_(u'количество (всего)'), default=1)
    quantity = models.IntegerField(_(u'количество (доступно)'), default=1)
    section = models.ForeignKey(Section, verbose_name=_(u'секция'))
    authors = models.ManyToManyField(Author, verbose_name=_(u'авторы'))
    room_only = models.BooleanField(_(u'Только читальный зал'), default=False)
    tags = TagAutocompleteField(u'Теги')
    owner = models.ForeignKey(Owner,
                              verbose_name=_(u'владелец'),
                              null=True, blank=True)

    class Meta:
        verbose_name = _(u"книга")
        verbose_name_plural = _(u"книги")
        ordering = ['title']

    def __unicode__(self):
        return self.title

# register(Book)


class Reader(models.Model):
    name = models.CharField(_(u'Имя'), max_length=512)
    phone = models.CharField(_(u'Телефон'),
                             max_length=64,
                             null=True, blank=True)
    email = models.CharField(_(u'Email'), max_length=64, null=True, blank=True)
    books = models.ManyToManyField(Book,
                                   through='Reading',
                                   verbose_name=_(u'книги'))

    class Meta:
        verbose_name = _(u"читатель")
        verbose_name_plural = _(u"читатели")
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Reading(models.Model):
    reader = models.ForeignKey(Reader, verbose_name=_(u'читатель'))
    book = models.ForeignKey(Book, verbose_name=_(u'книга'))
    took_at = models.DateField(_(u'Дата взятия'), db_index=True)
    returned_at = models.DateField(_(u'Дата возвращения'),
                                   db_index=True,
                                   default=None,
                                   null=True, blank=True)

    class Meta:
        verbose_name = _(u"взятая книга")
        verbose_name_plural = _(u"взятые книги")
        ordering = ['took_at']
