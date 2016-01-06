# -*- coding: utf-8 -*-
from tagging.models import Tag, TaggedItem
from django.views.generic import TemplateView, ListView
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.db.models import Q

from core import models


class ReadersView(ListView):
    template_name = "readers.html"
    paginate_by = 20

    def get_queryset(self):
        readers = models.Reader.objects.select_related().all()

        if 'q' in self.request.GET and self.request.GET['q']:
            q = self.request.GET['q']
            readers = readers.filter(name__icontains=q)

        return readers.order_by('name')

    def get_context_data(self, **kwargs):
        context = super(ReadersView, self).get_context_data(**kwargs)
        context['search'] = {
            'url': reverse('readers'),
            'place_holder': _(u'поиск читателя')
        }
        if 'q' in self.request.GET:
            context['q'] = self.request.GET['q']

        return context
