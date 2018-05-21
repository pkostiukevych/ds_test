from datetime import datetime, timedelta


def set_user_type(get_response):
    def middleware(request):
        if request.user and (request.user.is_staff or request.user.is_superuser):
            request.session['is_manager'] = True

        response = get_response(request)
        response.set_cookie(
            'is_manager', 1 if request.session.get('is_manager', False) else 0,
            expires=datetime.now() + timedelta(minutes=15)
        )
        return response

    return middleware

