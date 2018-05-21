from django.shortcuts import render

from ds_test.models import Request


def last_10_requests(request):
    items = Request.objects.all().order_by('-time')[:10]
    return render(request, 'books/requests.html', dict(requests=items))
