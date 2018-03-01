import sys
import subprocess
import re
from datetime import date

from bolognese.constants import EDITOR
from bolognese.core.recipe import Recipe
from bolognese.core.food import Food
from bolognese.core.diary import Diary
from bolognese.core.nutrients import Nutrients
from bolognese.core.config import Config

def get_totals(foodlist, foods = {}, recipes = {}):
    total = Nutrients()

    for item in foodlist.items:
        serving = item['servings'] if 'servings' in item else 1
        if 'recipe' in item:
            recipe_name = item['recipe']
            if recipe_name not in recipes:
                recipe = recipes[recipe_name] = Recipe(recipe_name)
                if not recipe.exists():
                    raise KeyError("The recipe '{}' does not exist".format(recipe_name))
                recipe.load()
            else:
                recipe = recipes[recipe_name]
            factor = recipe.servings.get_factor(serving)
            child_total = factor * get_totals(recipe.foodlist, foods, recipes)
        if 'food' in item:
            food_name = item['food']
            if food_name not in foods:
                food = foods[food_name] = Food(food_name)
                if not food.exists():
                    raise KeyError("The food '{}' does not exist".format(food_name))
                food.load()
            else:
                food = foods[food_name]
            factor = food.servings.get_factor(serving)
            child_total = factor * food.nutrients
        total = total + child_total

    return total

def root_handle(args):
    pass

def parse_date(s):
    prog = re.compile("(\d{4})[-.](\d{2})[-.](\d{2})")

    try:
        m = prog.match(s)
        if m is None:
            raise ValueError()
        d = date(*[int(m.group(i)) for i in range(1,4)])
    except:
        print("The given date should be in ISO format.", file=sys.stderr)
        return None

    return d

def edit_handle(args):
    date = parse_date(args.date)
    if date is None:
        return

    diary = Diary(date)
    subprocess.call([EDITOR, diary.path()])

def edit_register(parent):
    parser = parent.add_parser('edit')
    parser.add_argument('--date', type=str, default=str(date.today()), help='Set the number of foo')
    parser.set_defaults(func=edit_handle)

def show_handle(args):
    date = parse_date(args.date)
    if date is None:
        return

    diary = Diary(date)
    if diary.exists():
        diary.load()

    config = Config()
    if config.exists():
        config.load()

    current = get_totals(diary.foodlist)
    goal = config.nutrients
    left = goal - current

    row_format = "{:>15}" + "{:>12}" * 3
    print(row_format.format("", "current", "goal", "left"))
    print(row_format.format("kcal", round(current.kilocalories), round(goal.kilocalories), round(left.kilocalories)))
    print(row_format.format("kj", round(current.kilojoule), round(goal.kilojoule), round(left.kilojoule)))
    for nutr in Nutrients.NUTRIENTS:
        print(row_format.format(nutr, round(current[nutr]), round(goal[nutr]), round(left[nutr])))

def show_register(parent):
    parser = parent.add_parser('show')
    parser.add_argument('--date', type=str, default=str(date.today()), help='Set the number of foo')
    parser.set_defaults(func=show_handle)

def add_food_handle(args):
    date = parse_date(args.date)
    if date is None:
        return

    diary = Diary(date)
    food = Food(args.food)

    if not food.exists():
        print("The food '{}' does not exist.".format(args.food), file=sys.stderr)
        return

    food.load()
    if not food.servings.is_valid_serving(args.serving):
        print("The serving '{}' is not a valid serving for the given food.".format(args.serving), file=sys.stderr)
        return

    if diary.exists():
        diary.load()

    diary.add_food(food, args.serving)
    diary.save()

def add_food_register(parent):
    parser = parent.add_parser('add-food')
    parser.set_defaults(func=add_food_handle)
    parser.add_argument('food', type=str, help='Set the number of foo')
    parser.add_argument('serving', nargs="?", type=str, default='1', help='Set the number of foo')
    parser.add_argument('--date', type=str, default=str(date.today()), help='Set the number of foo')

def add_recipe_handle(args):
    date = parse_date(args.date)
    if date is None:
        return

    diary = Diary(date)
    recipe = Recipe(args.recipe)

    if not recipe.exists():
        print("The recipe '{}' does not exist.".format(args.recipe), file=sys.stderr)
        return

    recipe.load()
    if not recipe.servings.is_valid_serving(args.serving):
        print("The serving '{}' is not a valid serving for the given recipe.".format(args.serving), file=sys.stderr)
        return

    if diary.exists():
        diary.load()

    diary.add_recipe(recipe, args.serving, recursive = args.recursive)
    diary.save()

def add_recipe_register(parent):
    parser = parent.add_parser('add-recipe')
    parser.set_defaults(func=add_recipe_handle)
    parser.add_argument('recipe', type=str, help='Set the number of foo')
    parser.add_argument('serving', nargs="?", type=str, default='1', help='Set the number of foo')
    parser.add_argument('--date', type=str, default=str(date.today()), help='Set the number of foo')
    parser.add_argument('--recursive', action='store_true', help='Set the number of foo')

def register(parent):
    parser = parent.add_parser('diary', help='diary help')
    parser.set_defaults(func=root_handle)
    subparsers = parser.add_subparsers(help='subsub parser help')

    edit_register(subparsers)
    show_register(subparsers)
    add_food_register(subparsers)
    add_recipe_register(subparsers)

