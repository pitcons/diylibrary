# -*- coding: utf-8 -*-
from django.forms import ModelForm
from ajax_select import register, LookupChannel
from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField, AutoCompleteField
from ajax_select import make_ajax_field
from .models import Author, Section, Book


@register('author')
class AuthorLookup(LookupChannel):

    model = Author

    def get_query(self, q, request):
        return self.model.objects.filter(name__icontains=q)

    def format_item_display(self, item):
        return u"<span class='author'>%s</span>" % item.name


@register('section')
class SectionsLookup(LookupChannel):

    model = Section

    def get_query(self, q, request):
        return self.model.objects.filter(name__contains=q)

    def format_item_display(self, item):
        return u"<span class='section'>%s</span>" % item.name


class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = 'id',

    authors = AutoCompleteSelectMultipleField('author',
                                              label=u"Авторы",
                                              required=False,
                                              help_text="")
