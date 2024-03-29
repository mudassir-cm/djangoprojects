from django.shortcuts import redirect


def auth_middleware(get_response):
    def middleware(request):
        returnurl = request.META['PATH_INFO']
        if not request.session.get('customer'):
            return redirect(f'/store/user_login?return_url={returnurl}')
        response = get_response(request)
        return response


    return middleware
