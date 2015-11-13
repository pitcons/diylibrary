"""diylibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from core.views.books import BooksView
import core.views.rest as rest


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^books/', BooksView.as_view(), name="books"),
#    url(r'^api/book/new', RestView.as_view(), name="api_book_new"),
    url(r'^api/book/reserve', rest.book_reserve),
    url(r'^api/book/return', rest.book_return),
    url(r'^api/book/?', rest.book_get),
    url(r'^/?', BooksView.as_view(), name="books"),
]
