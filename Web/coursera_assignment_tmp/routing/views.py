from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_http_methods


@require_http_methods(["GET"])
def simple_route(request):
    return HttpResponse('')

