from django.contrib import admin
from django.urls import path
from . import views

app_name = 'manage'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.manage_list, name="home"),
]
