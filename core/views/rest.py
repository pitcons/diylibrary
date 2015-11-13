# -*- coding: utf-8 -*-
from django.http import JsonResponse, HttpResponseBadRequest
from django.db.models import F
from django.views.generic import View
from core.models import Book


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


def book_reserve(request):
    book = _get_book(request)
    if book.quantity <= 0:
        return HttpResponseBadRequest("Quantity can't be less than null")

    Book.objects.filter(id=book.id).update(quantity=F('quantity')-1)
    return JsonResponse({
            "quantity_total": book.quantity_total,
            "quantity": book.quantity - 1,
    })


def book_return(request):
    book = _get_book(request)
    if book.quantity >= book.quantity_total:
        return HttpResponseBadRequest("Quantity can't be more than total")

    Book.objects.filter(id=book.id).update(quantity=F('quantity')+1)
    return JsonResponse({
            "quantity_total": book.quantity_total,
            "quantity": book.quantity + 1,
    })
