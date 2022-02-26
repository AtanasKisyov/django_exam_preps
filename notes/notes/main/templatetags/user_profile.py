from django import template

from notes.main.helpers import get_user_profile

register = template.Library()


@register.simple_tag()
def user():
    user_profile = get_user_profile()
    if user_profile:
        return True
    return False
