from django.utils import timezone

from ds_test.models import Request


def save(get_response):
    def middleware(request):
        request_data = {
            'time': timezone.now(),
            'path': request.META.get('PATH_INFO'),
            'method': request.META.get('REQUEST_METHOD'),
            'protocol': request.META.get('SERVER_PROTOCOL'),
            'remote_addr': request.META.get('REMOTE_ADDR'),
            'http_user_agent': request.META.get('HTTP_USER_AGENT'),

        }
        response = get_response(request)
        request_data['response_status'] = response.status_code
        Request.objects.create(**request_data)
        return response

    return middleware
