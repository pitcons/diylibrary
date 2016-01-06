# -*- coding: utf-8 -*-
from tagging.models import Tag, TaggedItem
from django.views.generic import TemplateView, ListView
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.db.models import Q

from core import models


class ReadingView(ListView):
    template_name = "reading.html"
    paginate_by = 20

    def get_queryset(self):
        reading = models.Reading.objects.all()
        show_returned = self.request.GET.get('show_returned', False)

        if show_returned != 'true':
            reading = reading.exclude(returned_at__isnull=False)

        if 'q' in self.request.GET and self.request.GET['q']:
            q = self.request.GET['q']
            authors = models.Author.objects.filter(name__icontains=q)
            books = models.Book.objects.filter(Q(title__icontains=q) |
                                               Q(isbn__icontains=q) |
                                               Q(authors__in=authors))
            readers = models.Reader.objects.filter(name__icontains=q)
            reading = reading.filter(Q(book__in=books)|
                                     Q(reader__in=readers))

        return reading.order_by('took_at')

    def get_context_data(self, **kwargs):
        context = super(ReadingView, self).get_context_data(**kwargs)
        show_returned = self.request.GET.get('show_returned', False)
        context['search'] = {
            'url': reverse('reading'),
            'place_holder': _(u'поиск взятой книги'),
            'show_returned': show_returned,
        }
        if 'q' in self.request.GET:
            context['q'] = self.request.GET['q']

        return context
