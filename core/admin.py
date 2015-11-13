from django.contrib import admin
from .models import Author, Section, Book


class BookAdmin(admin.ModelAdmin):
    list_display = 'id', 'isbn', 'year',  'section', 'title', 'quantity', 'quantity_total'
    list_filter = 'year', 'section'
    search_fields = 'title',


admin.site.register(Author)
admin.site.register(Section)
admin.site.register(Book, BookAdmin)
