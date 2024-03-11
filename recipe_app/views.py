import logging
from random import sample

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, RecipeEditForm
from .models import Author, Category

from .forms import RecipeAddForm
from .models import Recipe

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'recipe_app/index.html')


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Author.objects.create(user=user)
            raw_password = form.cleaned_data.get('password1')
            logger.info(f'New user created {user=}')
            # authentication
            author = authenticate(username=user.username, password=raw_password)
            login(request, author)
            logger.info(f'User {author=} has authorized successfully')
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'recipe_app/signup.html', {'form': form})


@login_required  # for adding a recipe user needs to be authorized
def add_recipe(request):  # to make new recipe
    if request.method == 'POST':
        form = RecipeAddForm(request.POST, request.FILES)
        message = 'Data error'
        if form.is_valid():
            recipe_name = form.cleaned_data['recipe_name']
            recipe_description = form.cleaned_data['recipe_description']
            recipe_cooking_steps = form.cleaned_data['recipe_cooking_steps']
            recipe_cooking_time = form.cleaned_data['recipe_cooking_time']
            if request.user.is_authenticated:
                author, created = Author.objects.get_or_create(user=request.user)
                recipe_author = author
            recipe_category = form.cleaned_data['recipe_category']
            category, created = Category.objects.get_or_create(name=recipe_category)
            recipe_image = form.cleaned_data['recipe_image']
            logger.info(
                f'Received data: {recipe_name=}, {recipe_cooking_steps=}, {recipe_cooking_time=}, {recipe_author.user=}, '
                f'{recipe_category=}, {recipe_image=},')
            recipe = Recipe(name=recipe_name, description=recipe_description, cooking_steps=recipe_cooking_steps,
                            cooking_time=recipe_cooking_time, author=recipe_author, category=category,
                            img=recipe_image)
            recipe.save()
            message = 'Recipe has been successfully added!'
    else:
        form = RecipeAddForm()
        message = 'Fill the form!'
    return render(request, 'recipe_app/add_recipe.html', context={'form': form, 'message': message})


@login_required  # for changing the recipe user needs to be authorized
def edit_recipe(request, recipe_id):  # to change recipe
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.author.user == request.user:
        if request.method == 'POST':
            form = RecipeEditForm(request.POST, request.FILES, instance=recipe)
            if form.is_valid():
                form.save()
                return render(request, 'recipe_app/edit_recipe.html',
                              {'form': form, 'recipe': recipe, 'message': 'Recipe has been successfully changed!'})
        else:
            form = RecipeEditForm(instance=recipe)
        return render(request, 'recipe_app/edit_recipe.html',
                      {'form': form, 'recipe': recipe, 'message': 'Make some changes:'})


@login_required  # for removing the recipe user needs to be authorized
def delete_recipe(request, recipe_id):  # to delete recipe
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.author.user == request.user:
        recipe.delete()
        messages.success(request, 'Recipe has been successfully removed!')
        return redirect('/show_all_my_recipe/')
    else:
        return render(request, 'recipe_app/error_page.html',
                      {'message': 'Error has been raised, probably, you have no rights to delete it.'})


@login_required  # for watching the current user recipes user needs to be authorized
def show_all_my_recipes(request):  # to show all recipes of the current user
    clear_recipes = Recipe.objects.filter(author_id=request.user.id)
    logger.info(f'Recipes of {request.user=}  have been got successfully!')
    return render(request, 'recipe_app/show_all_my_recipe.html', {'clear_recipes': clear_recipes, 'user': request.user})


def show_five_recipes(request):  # to show 5 random recipes
    n = None
    my_ids = Recipe.objects.values_list('id', flat=True)
    my_ids = list(my_ids)
    if len(my_ids) < 5:
        # show all recipes when count of recipes below 5
        rand_ids = my_ids
        n = len(my_ids)
    else:
        rand_ids = sample(my_ids, 5)

    random_recipe = Recipe.objects.filter(id__in=rand_ids)
    logger.info(f'{n} random recipes с ID {rand_ids} have been got successfully.')

    return render(request, 'recipe_app/show_five_recipe.html',
                  {'random_recipe': random_recipe, 'message': f'{n} random recipes have been found'})


def show_the_recipe(request, recipe_id):  # show 1 recipe by id
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    logger.info(f'Recipe with ID:{recipe_id=} have been found: {recipe=}')
    return render(request, 'recipe_app/show_full_recipe.html', {'recipe': recipe})
