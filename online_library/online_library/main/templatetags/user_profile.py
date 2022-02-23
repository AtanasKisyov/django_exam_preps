from django import template

from online_library.main.models import Profile

register = template.Library()


@register.simple_tag()
def user_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return False
