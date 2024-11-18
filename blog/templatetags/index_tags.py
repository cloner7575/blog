# products_filters.py
from django import template
from django.utils import timezone
from persiantools.jdatetime import JalaliDate
register = template.Library()


@register.filter
def jalalidate(date):
    return JalaliDate(date).strftime('%Y/%m/%d')


@register.filter
def convert_num_to_k(num):
    if num > 999:
        return f'{num/1000}k'
    return num