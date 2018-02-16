import constants
import os
import sys
import subprocess
import yaml
from meal import Meal
from food import Food
from dictionary_helpers import update_dictionary

def root_handle(args):
    pass

def edit_handle(args):
    pass

def edit_register(parent):
    parser = parent.add_parser('edit')
    parser.set_defaults(func=edit_handle)
    parser.add_argument('--date', type=str, help='Set the number of foo')

def show_handle(args):
    pass

def show_register(parent):
    parser = parent.add_parser('show')
    parser.set_defaults(func=show_handle)
    parser.add_argument('--date', type=str, help='Set the number of foo')

def add_food_handle(args):
    pass

def add_food_register(parent):
    parser = parent.add_parser('add-food')
    parser.set_defaults(func=add_food_handle)
    parser.add_argument('food', type=str, help='Set the number of foo')
    parser.add_argument('--date', type=str, help='Set the number of foo')

def add_meal_handle(args):
    pass

def add_meal_register(parent):
    parser = parent.add_parser('add-meal')
    parser.set_defaults(func=add_meal_handle)
    parser.add_argument('meal', type=str, help='Set the number of foo')
    parser.add_argument('--date', type=str, help='Set the number of foo')

def register(parent):
    parser = parent.add_parser('diary', help='diary help')
    parser.set_defaults(func=root_handle)
    subparsers = parser.add_subparsers(help='subsub parser help')

    edit_register(subparsers)
    show_register(subparsers)
    add_food_register(subparsers)
    add_meal_register(subparsers)

    # remove, add, edit, log
