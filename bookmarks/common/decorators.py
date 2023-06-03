from django.http import HttpResponseBadRequest

## Django descontinuou o método is_ajax do objeto request
## para resolver esse problema, aqui está criado uma função
## para verificar se uma requisição HTTP foi feita por ajax
## https://groups.google.com/g/django-users/c/5x-qF0Q5Xi8?pli=1
## https://docs.djangoproject.com/en/3.1/releases/3.1/#id2
def is_ajax(request):
     return request.headers.get('x-requested-with') == 'XMLHttpRequest'

def ajax_required(f):
    def wrap(request, *args, **kwargs):
        if not is_ajax(request):
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap