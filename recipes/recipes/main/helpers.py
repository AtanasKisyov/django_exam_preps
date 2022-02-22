from django.core.exceptions import ValidationError

from recipes.main.models import Recipe


def validate_string_is_separated_correctly(value):
    for i in range(len(value)):
        ch = value[i]
        previous_char = value[i - 1]
        if ch == ' ' and previous_char != ',':
            raise ValidationError('All ingredients must be separated with ","!')


def get_recipe(pk):
    return Recipe.objects.get(pk=pk)
