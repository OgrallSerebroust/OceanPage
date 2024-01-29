from django import template
from typing import Any

register = template.Library()

@register.filter(name="entireweight")
def is_entire_weight(value) -> bool:
    if value % 1: 
        return False
    else:
        return True

@register.filter(name="tograms")
def weight_in_grams(value) -> Any:
    value = float(value)
    if value < 1.0:
        value *= 1000;
        return str(int(value)) + " гр";
    else:
        integer_part = int(value - value % 1)
        return str(integer_part) + " кг " + str(int((value % 1) * 1000)) + " гр"
