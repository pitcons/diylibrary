# -*- coding: utf-8 -*-
from tagging.models import Tag, TaggedItem
from django.views.generic import TemplateView, ListView
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.db.models import Q

from core import models


class BooksView(ListView):
    template_name = "books.html"
    paginate_by = 20

    def get_queryset(self):
        if 'tag' in self.request.GET and self.request.GET['tag']:
            tag = Tag.objects.get(name=self.request.GET['tag'])
            books = TaggedItem.objects.get_by_model(models.Book, tag).order_by('title')
        else:
            books = models.Book.objects.all().order_by('title')

        if 'section' in self.request.GET and self.request.GET['section']:
            books = books.filter(section__name=self.request.GET['section'])

        if 'q' in self.request.GET and self.request.GET['q']:
            q = self.request.GET['q']
            authors = models.Author.objects.filter(name__icontains=q)
            tags = Tag.objects.filter(name__contains=q)
            tagged_books = TaggedItem.objects.get_union_by_model(models.Book, tags)

            books = books.filter(Q(title__icontains=q) |
                                 Q(isbn__icontains=q) |
                                 Q(authors__in=authors)) | tagged_books

        return books.order_by('title')

    def get_context_data(self, **kwargs):
        context = super(BooksView, self).get_context_data(**kwargs)
        context['search'] = {
            'url': reverse('books'),
            'place_holder': _(u'поиск книги')
        }
        context['sections'] = models.Section.objects.order_by('name')
        context['readers'] = models.Reader.objects.all()

        if 'section' in self.request.GET:
            context['selected_section'] = self.request.GET['section']

        if 'q' in self.request.GET:
            context['q'] = self.request.GET['q']

        return context
