# products_filters.py
from django import template
from django.utils import timezone
from persiantools.jdatetime import JalaliDate
register = template.Library()


@register.filter
def jalalidate(date):
    return JalaliDate(date).strftime('%Y/%m/%d')
