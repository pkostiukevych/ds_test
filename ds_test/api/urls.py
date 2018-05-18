
from django.conf.urls import url
from ds_test.api.endpoints import *

urlpatterns = [
    url(r'^books$', book_api),
    url(r'^books/(?P<book_id>[0-9]+)$', book_api),
    url(r'^authors$', author_api),
    url(r'^authors/(?P<author_id>[0-9]+)$', author_api),
]
