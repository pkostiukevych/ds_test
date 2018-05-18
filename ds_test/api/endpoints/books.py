import json
from math import ceil

from django.http import JsonResponse, HttpResponseForbidden

from ds_test.models import Book, Author


def book_api(request, book_id=None):
    if request.method == 'GET':
        if book_id:
            try:
                book = Book.objects.prefetch_related('authors').get(id=book_id)
            except Book.DoesNotExist:
                return JsonResponse({'reason': 'book_not_found'}, status=404, safe=False)
            return JsonResponse(serializer(book), status=200, safe=False)
        else:
            page = int(request.GET.get('page', 1))
            books = Book.objects.prefetch_related('authors').all()
            books_count = books.count()

            if books_count and page > ceil(books_count / 50):
                return JsonResponse(
                    {'reason': 'exceeded_max_page_%s_for_total_%s_items' % (ceil(books_count / 50), books_count)},
                    safe=False, status=404
                )

            return JsonResponse(
                {
                    'total_books': books_count,
                    'page': page,
                    'data': list(map(serializer, books[50 * (page - 1): 50 * page])),
                },
                status=200, safe=False
            )

    if request.method == 'POST':
        # TODO add validation
        request_data = json.loads(request.body)
        if book_id:
            try:
                book = Book.objects.get(id=1)
            except Book.DoesNotExist:
                return JsonResponse(None, status=404, safe=False)
        else:
            book = Book()

        authors = Author.objects.filter(id__in=request_data.pop('authors', []))

        for attr, val in request_data.items():
            setattr(book, attr, val)
        book.save()
        book.authors.set(authors)
        return JsonResponse(serializer(book), status=201, safe=False)

    return HttpResponseForbidden(('GET', 'POST',))


def serializer(book):
    return {
        'id': book.id,
        'title': book.title,
        'authors': [author.full_name() for author in book.authors.all()],
        'isbn': book.isbn or '',
        'price': book.price
    }