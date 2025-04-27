from django.db import models


class Employee(models.Model):
    """
    Модель для представления работника
    """
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"


class Shift(models.Model):
    """
    Модель для представления рабочей смены
    """
    date = models.DateField(verbose_name="Дата")
    employee = models.ForeignKey(
            Employee,
            on_delete=models.CASCADE,
            related_name="shifts",
            verbose_name="Работник"
            )

    def __str__(self):
        return f"{self.date.strftime('%d.%m.%Y')} - {self.employee}"

    class Meta:
        verbose_name = "Смена"
        verbose_name_plural = "Смены"
        ordering = ['date']


class DesiredTimeOff(models.Model):
    """
    Модель для представления желаемых выходных дней
    """
    employee = models.ForeignKey(
            Employee,
            on_delete=models.CASCADE,
            related_name="desired_time_off",
            verbose_name="Работник"
            )
    date = models.DateField(verbose_name="Дата")

    class Meta:
        verbose_name = "Желаемый выходной"
        verbose_name_plural = "Желаемые выходные"
        unique_together = ('employee', 'date')

    def __str__(self):
        return f"{self.employee} - {self.date.strftime('%d.%m.%Y')}"


class WorkSummary(models.Model):
    """
    Модель для учета отработанных смен по месяцам
    """
    employee = models.ForeignKey(
            Employee,
            on_delete=models.CASCADE,
            related_name="work_summaries",
            verbose_name="Работник"
            )
    month = models.DateField(verbose_name="Месяц")
    shift_count = models.PositiveIntegerField(default=0, verbose_name="Количество смен")

    class Meta:
        verbose_name = "Итоги работы"
        verbose_name_plural = "Итоги работы"
        unique_together = ('employee', 'month')

    def __str__(self):
        return f"{self.employee} - {self.month.strftime('%B %Y')}: {self.shift_count} смен"
