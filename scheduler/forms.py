from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    """
    Форма для создания и редактирования сотрудника.
    """
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'is_active']
        labels = {
                'first_name': 'Имя',
                'last_name': 'Фамилия',
                'is_active': 'Активен'
                }
        widgets = {
                'first_name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите имя'
                    }),
                'last_name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите фамилию'
                    }),
                'is_active': forms.CheckboxInput(attrs={
                    'class': 'form-check-input'
                    })
                }
