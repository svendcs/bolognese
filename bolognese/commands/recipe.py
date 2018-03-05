import os
import sys
import subprocess

from bolognese.constants import EDITOR
from bolognese.core.recipe import Recipe
from bolognese.core.food import Food

def root_handle(args):
        for f in Recipe.list():
            print(f)

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
    parser.add_argument('--servings', type=str, nargs='+', help='Set the number of foo')

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
    parser.add_argument('--servings', type=str, nargs='+', help='Set the number of foo')

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
    vargs = vars(args)

    if not recipe.exists():
        print("The recipe '{}' does not exist.".format(args.recipe), file=sys.stderr)
        return

    if not food.exists():
        print("The food '{}' does not exist.".format(args.food), file=sys.stderr)
        return

    food.load()

    if not food.servings.is_valid_serving(args.serving):
        print("The serving '{}' is not a valid serving for the given food.".format(args.serving), file=sys.stderr)
        return

    recipe.load()
    recipe.add_food(food, args.serving)
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
    vargs = vars(args)

    if not recipe.exists():
        print("The recipe '{}' does not exist.".format(args.recipe), file=sys.stderr)
        return

    if not subrecipe.exists():
        print("The recipe '{}' does not exist.".format(args.subrecipe), file=sys.stderr)
        return

    subrecipe.load()

    if not subrecipe.servings.is_valid_serving(args.serving):
        print("The serving '{}' is not a valid serving for the given recipe.".format(args.serving), file=sys.stderr)
        return

    recipe.load()
    recipe.add_recipe(subrecipe, args.serving)
    recipe.save()

def add_recipe_register(parent):
    parser = parent.add_parser('add-recipe')
    parser.set_defaults(func=add_recipe_handle)
    parser.add_argument('recipe', type=str, help='Set the number of foo')
    parser.add_argument('subrecipe', type=str, help='Set the number of foo')
    parser.add_argument('serving', nargs="?", type=str, default='1', help='Set the number of foo')

def register(parent):
    parser = parent.add_parser('recipe', help='recipe help')
    parser.set_defaults(func=root_handle)
    subparsers = parser.add_subparsers(help='subsub parser help')

    edit_register(subparsers)
    add_register(subparsers)
    copy_register(subparsers)
    move_register(subparsers)
    remove_register(subparsers)
    add_food_register(subparsers)
    add_recipe_register(subparsers)

