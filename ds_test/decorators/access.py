from django.shortcuts import redirect


def manager_only(view):
    def check(request, *args, **kwars):
        if request.session.get('is_manager', False):
            return view(request, *args, **kwars)
        else:
            return redirect('/')

    return check
