import os
import sys
import subprocess

from bolognese.constants import EDITOR
from bolognese.core.recipe import Recipe
from bolognese.core.food import Food
from bolognese.core.serving import Serving

def edit_handle(args):
    recipe = Recipe(args.recipe)
    vargs = vars(args)

    if args.servings is None:
        subprocess.call([EDITOR, recipe.path()])
    else:
        if recipe.exists():
            recipe.load()
        recipe.update(vargs)
        recipe.save()

def edit_register(parent):
    parser = parent.add_parser('edit')
    parser.set_defaults(func=edit_handle)
    parser.add_argument('recipe', type=str, help='Set the number of foo')
    parser.add_argument('--servings', type=Serving, nargs='+', help='Set the number of foo')

def add_handle(args):
    recipe = Recipe(args.recipe)
    vargs = vars(args)

    if recipe.exists():
        print("The recipe '{}' already exists.".format(args.recipe), file=sys.stderr)
        return

    if args.servings is None:
        recipe.save()
        subprocess.call([EDITOR, recipe.path()])
    else:
        recipe.update(vargs)
        recipe.save()

def add_register(parent):
    parser = parent.add_parser('add')
    parser.set_defaults(func=add_handle)
    parser.add_argument('recipe', type=str, help='Set the number of foo')
    parser.add_argument('--servings', type=Serving, nargs='+', help='Set the number of foo')

def copy_handle(args):
    recipe = Recipe(args.recipe)
    new_recipe = Recipe(args.new_name)

    if not recipe.exists():
        print("The recipe '{}' does not exist.".format(args.recipe), file=sys.stderr)
        return

    if new_recipe.exists():
        print("The recipe '{}' already exists.".format(args.new_name), file=sys.stderr)
        return

    recipe.load()
    recipe.name = args.new_name
    recipe.save()

def copy_register(parent):
    remove_parser = parent.add_parser('copy')
    remove_parser.set_defaults(func=copy_handle)
    remove_parser.add_argument('recipe', type=str, help='Set the number of foo')
    remove_parser.add_argument('new_name', type=str, help='Set the number of foo')

def move_handle(args):
    recipe = Recipe(args.recipe)
    new_recipe = Recipe(args.new_name)

    if not recipe.exists():
        print("The recipe '{}' does not exist.".format(args.recipe), file=sys.stderr)
        return

    if new_recipe.exists():
        print("The recipe '{}' already exists.".format(args.new_name), file=sys.stderr)
        return

    recipe.load()
    recipe.remove()
    recipe.name = args.new_name
    recipe.save()

def move_register(parent):
    remove_parser = parent.add_parser('move')
    remove_parser.set_defaults(func=move_handle)
    remove_parser.add_argument('recipe', type=str, help='Set the number of foo')
    remove_parser.add_argument('new_name', type=str, help='Set the number of foo')

def remove_handle(args):
    recipe = Recipe(args.recipe)

    if not recipe.exists():
        print("The recipe '{}' does not exist.".format(args.recipe), file=sys.stderr)
    else:
        recipe.remove()

def remove_register(parent):
    remove_parser = parent.add_parser('remove')
    remove_parser.set_defaults(func=remove_handle)
    remove_parser.add_argument('recipe', type=str, help='Set the number of foo')

def add_food_handle(args):
    recipe = Recipe(args.recipe)
    food = Food(args.food)
    serving = Serving.from_string(args.serving)
    vargs = vars(args)

    if not recipe.exists():
        print("The recipe '{}' does not exist.".format(args.recipe), file=sys.stderr)
        return

    if not food.exists():
        print("The food '{}' does not exist.".format(args.food), file=sys.stderr)
        return

    food.load()

    if not food.servings.compatible(serving):
        print("The serving '{}' is not a valid serving for the given food.".format(serving), file=sys.stderr)
        return

    recipe.load()
    recipe.add_food(food, serving)
    recipe.save()

def add_food_register(parent):
    parser = parent.add_parser('add-food')
    parser.set_defaults(func=add_food_handle)
    parser.add_argument('recipe', type=str, help='Set the number of foo')
    parser.add_argument('food', type=str, help='Set the number of foo')
    parser.add_argument('serving', nargs="?", type=str, default='1', help='Set the number of foo')

def add_recipe_handle(args):
    recipe = Recipe(args.recipe)
    subrecipe = Recipe(args.subrecipe)
    serving = Serving.from_string(args.serving)
    vargs = vars(args)

    if not recipe.exists():
        print("The recipe '{}' does not exist.".format(args.recipe), file=sys.stderr)
        return

    if not subrecipe.exists():
        print("The recipe '{}' does not exist.".format(args.subrecipe), file=sys.stderr)
        return

    subrecipe.load()

    if not subrecipe.servings.compatible(serving):
        print("The serving '{}' is not a valid serving for the given recipe.".format(serving), file=sys.stderr)
        return

    recipe.load()
    recipe.add_recipe(subrecipe, serving)
    recipe.save()

def add_recipe_register(parent):
    parser = parent.add_parser('add-recipe')
    parser.set_defaults(func=add_recipe_handle)
    parser.add_argument('recipe', type=str, help='Set the number of foo')
    parser.add_argument('subrecipe', type=str, help='Set the number of foo')
    parser.add_argument('serving', nargs="?", type=str, default='1', help='Set the number of foo')

def list_handle(args):
    for r in Recipe.list():
        print(r)

def list_register(parent):
    import_parser = parent.add_parser('list')
    import_parser.set_defaults(func=list_handle)

def register(parent):
    parser = parent.add_parser('recipe', help='recipe help')
    subparsers = parser.add_subparsers(help='subsub parser help')

    edit_register(subparsers)
    add_register(subparsers)
    copy_register(subparsers)
    move_register(subparsers)
    remove_register(subparsers)
    add_food_register(subparsers)
    add_recipe_register(subparsers)
    list_register(subparsers)

