import datetime

from django.utils import timezone
from django.shortcuts import (
        render,
        get_object_or_404,
        redirect
        )
from .models import (
        Employee,
        Shift,
        WorkSummary,
        DesiredTimeOff
        )

from .forms import EmployeeForm


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
    return render(request, 'scheduler/index.html')


def current_schedule(request):
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
    return render(request, 'scheduler/current_schedule.html', context)


def desired_schedule(request):
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

    return render(request, 'scheduler/desired_schedule.html', context)


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
    return render(request, 'scheduler/work_summary.html', context)


def employee_form(request, employee_id=None):
    """
    Создания и редактирования сотрудника.
    """
    if employee_id:
        employee = get_object_or_404(Employee, id=employee_id)
    else:
        employee = None

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('scheduler:current_schedule')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'scheduler/employee_form.html', {
        'form': form,
        'employee': employee
        })


def employee_delete(request):
    """
    Удаление сотрудника
    """
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        employee = get_object_or_404(Employee, id=employee_id)
        employee.delete()
        return redirect('scheduler:current_schedule')
        
    employees = Employee.objects.all().order_by('last_name', 'first_name')
    return render(request, 'scheduler/employee_delete.html', {
        'employees': employees
    })

