from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse

import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def myapp_index(request):
    str = "str"
    return TemplateResponse(request, 'myapp/index.html', {'str': str})
    # return HttpResponse('AAA')

