from django.urls import path
from django.shortcuts import redirect

from . import views


app_name = 'sheduler'

urlpatterns = [
        path('', lambda _: redirect('sheduler:current_shedule'), name='index'),
        path('current/', views.current_shedule, name='current_shedule'),
        path('desired/', views.desired_shedule, name='desired_shedule'),
        path('summary/', views.work_summary, name='work_summary'),
        ]

