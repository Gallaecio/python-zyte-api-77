from django.http import HttpResponse

from .utils import omnifollow_product_extract

def zyte_test(request):
    omnifollow_product_extract("")
    return HttpResponse("success")