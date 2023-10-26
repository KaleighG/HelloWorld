from django.http.response import HttpResponse
from django.http.request import HttpRequest
# Create your views here.
def hello_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello World!')