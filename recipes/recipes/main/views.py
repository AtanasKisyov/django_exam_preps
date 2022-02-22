from django.shortcuts import render, redirect

from recipes.main.forms import CreateRecipe, EditRecipe, DeleteRecipe
from recipes.main.helpers import get_recipe
from recipes.main.models import Recipe


def home(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'POST':
        form = CreateRecipe(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateRecipe()

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = get_recipe(pk)
    if request.method == 'POST':
        form = EditRecipe(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditRecipe(instance=recipe)
    context = {
        'form': form,
    }
    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = get_recipe(pk)
    if request.method == 'POST':
        form = DeleteRecipe(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeleteRecipe(instance=recipe)
    context = {
        'form': form,
    }
    return render(request, 'delete.html', context)


def details_recipe(request, pk):
    recipe = get_recipe(pk)
    ingredients = recipe.ingredients.split(',')
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'details.html', context)
