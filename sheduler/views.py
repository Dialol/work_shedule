from django.shortcuts import render
from .models import (
        Employee,
        Shift,
        WorkSummary,
        DesiredTimeOff
        )
from django.utils import timezone
import datetime


def get_week_range(date=None, next_week=False):
    """
    Период текущей недели (понедельник - воскресенье).
    """
    if date is None:
        date = timezone.now().date()
    
    if next_week:
        date = date + datetime.timedelta(days=7)

    start_of_week = date - datetime.timedelta(days=date.weekday())
    end_of_week = start_of_week + datetime.timedelta(days=6)
    
    days = []
    current = start_of_week
    while current <= end_of_week:
        days.append(current)
        current += datetime.timedelta(days=1)

    return start_of_week, end_of_week, days


def get_active_employees():
    """
    Список активных сотрудников
    """
    return Employee.objects.filter(is_active=True)


def index(request):
    """
    Главная страница с навигацией
    """
    return render(request, 'sheduler/index.html')


def current_shedule(request):
    """
    Текущий график работы
    """
    start_of_week, end_of_week, days = get_week_range()
    shifts = Shift.objects.filter(
            date__range=[start_of_week, end_of_week]).order_by('date')
    
    shifts_by_day = {}
    for day in days:
        shifts_by_day[day] = shifts.filter(date=day)
    
    employees = get_active_employees()

    context = {
        'shifts_by_day': shifts_by_day,
        'start_of_week': start_of_week,
        'end_of_week': end_of_week,
        'employees': employees,
    }
    return render(request, 'sheduler/current_shedule.html', context)


def desired_shedule(request):
    """
    Форма для ввода желаемых выходных
    """
    start_of_week, end_of_week, days = get_week_range(next_week=True)

    employees = get_active_employees()

    if request.method == 'POST':
        DesiredTimeOff.objects.filter(
                date__range=[start_of_week, end_of_week]
                ).delete()

        for employee in employees:
            for day in days:
                day_str = day.strftime('%Y-%m-%d')
                checkbox_name = f"timeoff_{employee.id}_{day_str}"

                if checkbox_name in request.POST:
                    DesiredTimeOff.objects.create(
                            employee=employee,
                            date=day
                            )

    desired_off = DesiredTimeOff.objects.filter(
            date__range=[start_of_week, end_of_week]
            )

    employee_days_off = {}
    for employee in employees:
        employee_days_off[employee.id] = [
                off.date for off in desired_off.filter(employee=employee)
                ]

    context = {
            'employees': employees,
            'days': days,
            'employee_days_off': employee_days_off,
            'start_of_week': start_of_week,
            'end_of_week': end_of_week,
            }

    return render(request, 'sheduler/desired_shedule.html', context)


def work_summary(request):
    """
    Отработанные смены по месяцам
    """
    employees = Employee.objects.all()
    summaries = WorkSummary.objects.all().order_by('-month')
    
    context = {
        'employees': employees,
        'summaries': summaries,
    }
    return render(request, 'sheduler/work_summary.html', context)
