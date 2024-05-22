from django import template

register = template.Library()

@register.filter
def contains(value, substring):
    """
    Checks if the given substring is in the value.
    Usage: {{ some_string|contains:"substring" }}
    """
    return substring in value
