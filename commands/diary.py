import constants
import os
import sys
import subprocess
import yaml
import re
from datetime import date
from meal import Meal
from food import Food
from diary import Diary
from dictionary_helpers import update_dictionary

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
    subprocess.call([constants.EDITOR, diary.path()])

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
    print(diary.foodlist.items)

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

    diary.add_food(args.food, args.serving)
    diary.save()

def add_food_register(parent):
    parser = parent.add_parser('add-food')
    parser.set_defaults(func=add_food_handle)
    parser.add_argument('food', type=str, help='Set the number of foo')
    parser.add_argument('serving', nargs="?", type=str, default='1', help='Set the number of foo')
    parser.add_argument('--date', type=str, default=str(date.today()), help='Set the number of foo')

def add_meal_handle(args):
    date = parse_date(args.date)
    if date is None:
        return

    diary = Diary(date)
    meal = Meal(args.meal)

    if not meal.exists():
        print("The meal '{}' does not exist.".format(args.meal), file=sys.stderr)
        return

    meal.load()
    if not meal.servings.is_valid_serving(args.serving):
        print("The serving '{}' is not a valid serving for the given meal.".format(args.serving), file=sys.stderr)
        return

    if diary.exists():
        diary.load()

    diary.add_meal(args.meal, args.serving)
    diary.save()

def add_meal_register(parent):
    parser = parent.add_parser('add-meal')
    parser.set_defaults(func=add_meal_handle)
    parser.add_argument('meal', type=str, help='Set the number of foo')
    parser.add_argument('serving', nargs="?", type=str, default='1', help='Set the number of foo')
    parser.add_argument('--date', type=str, default=str(date.today()), help='Set the number of foo')

def register(parent):
    parser = parent.add_parser('diary', help='diary help')
    parser.set_defaults(func=root_handle)
    subparsers = parser.add_subparsers(help='subsub parser help')

    edit_register(subparsers)
    show_register(subparsers)
    add_food_register(subparsers)
    add_meal_register(subparsers)

