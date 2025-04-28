from django.urls import path
from django.shortcuts import redirect

from . import views


app_name = 'scheduler'

urlpatterns = [
        path('', lambda _: redirect('scheduler:current_schedule'), name='index'),
        path('current/', views.current_schedule, name='current_schedule'),
        path('desired/', views.desired_schedule, name='desired_schedule'),
        path('summary/', views.work_summary, name='work_summary'),
        path(
            'employee/add/',
            views.employee_form,
            name='employee_add'
            ),
        path(
            'employee/<int:employee_id>/edit/',
            views.employee_form,
            name='employee_edit'
            ),
        path('employee/delete/',
             views.employee_delete,
             name='employee_delete'
             ),
        ]
