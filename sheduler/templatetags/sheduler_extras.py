"""
Фильтры для шаблонов приложения.
"""
from django import template


register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Фильтр для получения элемента словаря по ключу в шаблоне.
    """
    return dictionary.get(key, [])
