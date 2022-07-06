import json
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from manage.models import User, Attendance
from pprint import pprint

@csrf_exempt
@require_http_methods(["GET", "POST"])
def arrival(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        pprint(params)
        attendance = Attendance.objects.create(
            user_name=params["user_name"]
        )
        return JsonResponse({'message': 'success'}, safe=False)
    else:
        items = [att.to_dict() for att in Attendance.objects.all()]

        return JsonResponse(items, safe=False)

@csrf_exempt
def delete(request):
    Attendance.objects.all().delete()
    return JsonResponse({'message': 'Deleted'})
