from django import template

register = template.Library()

@register.filter
def get_comment_num(obj):
    return obj.get_comment_num()


@register.filter
def get_like_num(obj):
    return obj.get_like_num()

@register.filter
def get_all_comment(obj):
    return obj.get_all_comment()

@register.filter
def if_current_user_liked(obj, user_id):
    return obj.if_current_user_liked(user_id=user_id)

