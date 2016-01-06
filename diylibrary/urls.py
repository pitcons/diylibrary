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
from django.contrib.auth.decorators import login_required
from core.views.books import BooksView
from core.views.reading import ReadingView
from core.views.readers import ReadersView
import core.views.rest as rest


urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^books/', BooksView.as_view(), name="books"),
#    url(r'^api/book/new', RestView.as_view(), name="api_book_new"),
    url(r'^api/book/reserve', rest.book_reserve),
    url(r'^api/reading/return', rest.reading_return),
    url(r'^api/reading/undo', rest.reading_undo),
    url(r'^api/book/?', rest.book_get),
    url(r'^api/reader/all', rest.readers_all),
    url(r'^reading/?',
        login_required(ReadingView.as_view()),
        name="reading"),
    url(r'^reader/?',
        login_required(ReadersView.as_view()),
        name="readers"),
    url(r'^/?',
        BooksView.as_view(),
        name="books"),
]
