# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.contrib import admin
from .models import Author, Section, Book, Reader, Reading, Owner


class BookAdmin(admin.ModelAdmin):
    list_display = 'id', 'isbn', 'year',  'section', 'title', 'quantity', 'quantity_total'
    list_filter = 'year', 'section', 'owner'
    search_fields = 'title',
    filter_horizontal = 'authors',


# class BookInline(admin.TabularInline):
#     model = Book.authors.through
#     extra = 0


class AuthorAdmin(admin.ModelAdmin):
    search_fields = 'name',
    # inlines = BookInline,


class ReaderAdmin(admin.ModelAdmin):
    search_fields = 'name', 'phone', 'email'
    list_display = 'name', 'phone', 'email'


class ReadingAdmin(admin.ModelAdmin):
    list_display = 'took_at', 'returned_at', 'reader', 'book'


class OwnerAdmin(admin.ModelAdmin):
    list_display = 'name',


admin.site.register(Author, AuthorAdmin)
admin.site.register(Section)
admin.site.register(Book, BookAdmin)
admin.site.register(Reader, ReaderAdmin)
admin.site.register(Reading, ReadingAdmin)
admin.site.register(Owner, OwnerAdmin)

admin.site.site_header = _(u'Каталог Цеткин')
