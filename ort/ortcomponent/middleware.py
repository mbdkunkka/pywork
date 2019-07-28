from django.http import HttpResponseRedirect
try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("拦截" + request.path)
        user = request.session.get('ort_user')
        if user:
            return None
        else:
            if request.path == '/ortcomponent/login/':
                return None
            else:
                return HttpResponseRedirect('/ortcomponent/login/')
