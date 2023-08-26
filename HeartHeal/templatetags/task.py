from django import template

register = template.Library()

@register.filter
def get_progress_value(obj):
    return obj.get_progress_value()


@register.filter
def get_all_tasks(obj):
    return obj.get_all_tasks()
