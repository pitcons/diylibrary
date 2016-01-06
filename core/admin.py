from django.contrib import admin
from .models import Author, Section, Book, Reader, Reading


class BookAdmin(admin.ModelAdmin):
    list_display = 'id', 'isbn', 'year',  'section', 'title', 'quantity', 'quantity_total'
    list_filter = 'year', 'section'
    search_fields = 'title',


class ReaderAdmin(admin.ModelAdmin):
    search_fields = 'name',


class ReadingAdmin(admin.ModelAdmin):
    list_display = 'took_at', 'returned_at', 'reader', 'book'


admin.site.register(Author)
admin.site.register(Section)
admin.site.register(Book, BookAdmin)
admin.site.register(Reader, ReaderAdmin)
admin.site.register(Reading, ReadingAdmin)
