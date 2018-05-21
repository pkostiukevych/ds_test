from django.shortcuts import render

from ds_test.decorators.access import manager_only


def list_books(request):
    return render(request, 'books/list.html')


@manager_only
def edit_or_create_book(request, book_id=None):
    return render(request, 'books/edit.html')

