from django.urls import path

from recipes.main.views import home, create_recipe, edit_recipe, delete_recipe, details_recipe

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_recipe, name='create_recipe'),
    path('edit/int:<pk>', edit_recipe, name='edit_recipe'),
    path('delete/int:<pk>', delete_recipe, name='delete_recipe'),
    path('details/int:<pk>', details_recipe, name='details_recipe'),
]
