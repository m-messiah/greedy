# coding=utf-8
__author__ = 'm_messiah'
from django import template

register = template.Library()

@register.filter
def count_unposted(values):
    return len(values) - len(values.filter(is_posted=True))