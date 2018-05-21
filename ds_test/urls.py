
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from ds_test.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', list_books),
    url(r'requests$', last_10_requests),
    url(r'edit/(?P<book_id>[0-9]+)$', edit_or_create_book),
    url(r'create$', edit_or_create_book),
    url(r'^api/', include('ds_test.api.urls')),
]
