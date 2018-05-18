from django.shortcuts import render


def list_books(request):
    return render(request, 'books/list.html')


def edit_or_create_book(request, book_id=None):
    return render(request, 'books/edit.html')

