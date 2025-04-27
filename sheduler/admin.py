from django.contrib import admin
from .models import Employee, Shift, DesiredTimeOff, WorkSummary


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Панель для управления работниками.
    """
    list_display = ('first_name', 'last_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name')


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    """
    Панель для управления сменами.
    """
    list_display = ('date', 'employee')
    list_filter = ('date', 'employee')
    date_hierarchy = 'date'


@admin.register(DesiredTimeOff)
class DesiredTimeOffAdmin(admin.ModelAdmin):
    """
    Панель для управления желаемыми выходными.
    """
    list_display = ('employee', 'date')
    list_filter = ('date', 'employee')
    date_hierarchy = 'date'


@admin.register(WorkSummary)
class WorkSummaryAdmin(admin.ModelAdmin):
    """
    Панель для управления итогами работы.
    """
    list_display = ('employee', 'month_display', 'shift_count')
    list_filter = ('month', 'employee')

    @admin.display(
            description='Месяц',
            ordering='month',
            )
    def month_display(self, obj):
        """
        Форматируем дату месяц в читаемый вид.
        """
        return obj.month.strftime('%B %Y')
