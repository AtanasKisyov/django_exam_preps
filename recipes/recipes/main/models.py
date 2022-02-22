from django.db import models

from recipes.main.helpers import validate_string_is_separated_correctly


class Recipe(models.Model):

    title = models.CharField(max_length=30)
    image_url = models.URLField()
    description = models.TextField()
    ingredients = models.CharField(max_length=250, validators=(validate_string_is_separated_correctly,))
    time = models.IntegerField()
