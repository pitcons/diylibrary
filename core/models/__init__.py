# -*- coding: utf-8 -*-
# http://www.isbnsearch.org/
from django.db import models
from tagging.registry import register


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    isbn = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=512)
    year = models.IntegerField(null=True, blank=True)
    quantity_total = models.IntegerField(default=1)
    quantity = models.IntegerField(default=1)
    section = models.ForeignKey(Section)
    authors = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.title

register(Book)


class Reader(models.Model):
    name = models.CharField(max_length=512)
    books = models.ManyToManyField(Book, through='Reading')

    def __unicode__(self):
        return self.name


class Reading(models.Model):
    reader = models.ForeignKey(Reader)
    book = models.ForeignKey(Book)
    took_at = models.DateField()
    returned_at = models.DateField(default=None,
                                   null=True,
                                   blank=True)
