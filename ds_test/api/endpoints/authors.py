from django.http import JsonResponse, HttpResponseForbidden

from ds_test.models import Author
from ds_test.api.serializers import author_serializer as serializer


def author_api(request, author_id=None):
    if request.method == 'GET':
        if author_id:
            try:
                author = Author.objects.get(id=author_id)
            except Author.DoesNotExist:
                return JsonResponse(None, status=404, safe=False)

            return JsonResponse(serializer(author), status=200, safe=False)
        else:
            authors = Author.objects.all()
            return JsonResponse(
                list(map(serializer, authors)),
                status=200, safe=False
            )

    if request.method == 'POST':
        if author_id:
            try:
                author = Author.objects.get(id=author_id)
            except Author.DoesNotExist:
                return JsonResponse(None, status=404, safe=False)

    return HttpResponseForbidden(('GET', 'POST',))

