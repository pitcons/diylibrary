# -*- coding: utf-8 -*-
import json
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.template import defaultfilters
from django.utils.translation import ugettext as _
from django.db.models import F
from django.views.generic import View
from core.models import Book, Reader, Reading

def _get_post(request):
    post = json.loads(request.body)
    post.update(request.POST)
    return post

def _get_book(request):
    if 'id' in request.GET:
        book = Book.objects.get(id=request.GET['id'])
    elif 'isbn' in request.GET:
        book = Book.objects.get(id=request.GET['isbn'])
    else:
        pass
    return book


def book_get(request):
    book = _get_book(request)
    return JsonResponse({
            "title": book.title,
            "year": book.year,
            "quantity_total": book.quantity_total,
            "quantity": book.quantity,
            "authors": [
                author.name for author in book.authors.all()
            ]
    })


@login_required
def book_reserve(request):
    book = _get_book(request)
    reader = Reader.objects.filter(id=request.GET['reader_id']).first()
    if not book:
        return HttpResponseBadRequest("Book isn't found.")
    if not reader:
        return HttpResponseBadRequest("Reader isn't found.")
    if book.quantity <= 0:
        return HttpResponseBadRequest("Quantity can't be less than null.")

    Reading(reader=reader, book=book, took_at=datetime.now()).save()
    Book.objects.filter(id=book.id).update(quantity=F('quantity')-1)
    return JsonResponse({
            "quantity_total": book.quantity_total,
            "quantity": book.quantity - 1,
    })


@login_required
def reading_return(request):
    if 'id' not in request.GET:
        return JsonResponse({
            'error': _(u'Отсуствует обязательный параметр id.')
        })
    reading = Reading.objects.select_related().get(id=request.GET['id'])
    if reading.returned_at:
        return JsonResponse({
            'error': _(u'Книга уже возвращена.')
        })

    returned_at = datetime.now()
    Reading.objects.filter(id=reading.id).update(returned_at=returned_at)
    Book.objects.filter(id=reading.book_id).update(quantity=F('quantity')+1)
    return JsonResponse({
        "quantity_total": reading.book.quantity_total,
        "quantity": reading.book.quantity + 1,
        "returned_at": defaultfilters.date(returned_at,
                                           "DATE_FORMAT")
    })


@login_required
def reading_undo(request):
    if 'id' not in request.GET:
        return JsonResponse({
            'error': _(u'Отсуствует обязательный параметр id.')
        })
    reading = Reading.objects.select_related().get(id=request.GET['id'])
    if not reading.returned_at:
        return JsonResponse({
            'error': _(u'Книга ещё не возвращена.')
        })

    Reading.objects.filter(id=reading.id).update(returned_at=None)
    Book.objects.filter(id=reading.book_id).update(quantity=F('quantity') - 1)
    return JsonResponse({
        "quantity_total": reading.book.quantity_total,
        "quantity": reading.book.quantity - 1,
    })


@login_required
def readers_all(request):
    return JsonResponse({
        'readers': [
            {'id': reader.id, 'name': reader.name}
            for reader in Reader.objects.all()
        ]
    })


@login_required
def reader_new(request):
    post = _get_post(request)
    if 'name' not in post:
        return JsonResponse({
            'error': 'Параметр name обязателен'
        })
    if Reader.objects.filter(name=post['name']).exists():
        return JsonResponse({
            'error': 'Читатель с таким именем уже сущетвует'
        })

    reader = Reader(name=post['name'],
                    phone=post.get('phone'),
                    email=post.get('email'))
    reader.save()
    return JsonResponse({
        'id': reader.id,
        'name': reader.name,
    })
