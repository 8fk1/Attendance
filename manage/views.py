from django.shortcuts import render
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from manage.models import User, Attendance

def manage_list(request):

    attendances = Attendance.objects.all()

    return TemplateResponse(request, 'manage/list.html', {'attendances': attendances})


