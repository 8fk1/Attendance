from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.myapp_index, name="home"),
    # path('arrival/', views.arrival, name='arrival'),
]
