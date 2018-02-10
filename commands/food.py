import constants
import os
import sys
import subprocess
import yaml
from food import Food
from dictionary_helpers import update_dictionary

def root_handle(args):
    for f in Food.list():
        print(f)

def edit_handle(args):
    food = Food(args.food)
    vargs = vars(args)

    if args.carbs is None and args.fat is None and args.protein is None and args.alcohol is None and args.servings is None:
        subprocess.call([constants.EDITOR, food.path()])
    else:
        if food.exists():
            food.load()
        food.update(vargs)
        food.save()

def edit_register(parent):
    edit_parser = parent.add_parser('edit')
    edit_parser.set_defaults(func=edit_handle)
    edit_parser.add_argument('food', type=str, help='Set the number of foo')
    edit_parser.add_argument('--carbs', type=int, help='Set the number of foo')
    edit_parser.add_argument('--protein', type=int, help='Set the number of foo')
    edit_parser.add_argument('--fat', type=int, help='Set the number of foo')
    edit_parser.add_argument('--alcohol', type=int, help='Set the number of foo')
    edit_parser.add_argument('--servings', type=str, nargs='+', help='Set the number of foo')

def add_handle(args):
    food = Food(args.food)
    vargs = vars(args)

    if food.exists():
        print("The food '{}' already exists.".format(args.food), file=sys.stderr)
        return

    if args.carbs is None and args.fat is None and args.protein is None and args.alcohol is None and args.servings is None:
        subprocess.call([constants.EDITOR, food.path()])
    else:
        food.update(vargs)
        food.save()

def add_register(parent):
    add_parser = parent.add_parser('add')
    add_parser.set_defaults(func=add_handle)
    add_parser.add_argument('food', type=str, help='Set the number of foo')
    add_parser.add_argument('--carbs', type=int, help='Set the number of foo')
    add_parser.add_argument('--protein', type=int, help='Set the number of foo')
    add_parser.add_argument('--fat', type=int, help='Set the number of foo')
    add_parser.add_argument('--alcohol', type=int, help='Set the number of foo')
    add_parser.add_argument('--servings', type=str, nargs='+', help='Set the number of foo')

def log_handle(args):
    print("Log handler")

def log_register(parent):
    log_parser = parent.add_parser('log')
    log_parser.set_defaults(func=log_handle)
    log_parser.add_argument('food', type=str, help='Set the number of foo')
    log_parser.add_argument('amount', type=str, help='Set the number of foo')

def remove_handle(args):
    food = Food(args.food)

    if not food.exists():
        print("The food '{}' does not exist.".format(args.food), file=sys.stderr)
    else:
        food.remove()

def remove_register(parent):
    remove_parser = parent.add_parser('remove')
    remove_parser.set_defaults(func=remove_handle)
    remove_parser.add_argument('food', type=str, help='Set the number of foo')

def import_handle(args):
    print("Import handler")

def import_register(parent):
    import_parser = parent.add_parser('import')
    import_parser.set_defaults(func=import_handle)
    import_parser.add_argument('database', type=str, help='Set the number of foo')
    import_parser.add_argument('id', type=str, help='Set the number of foo')
    import_parser.add_argument('food', type=str, help='Set the number of foo')

def register(parent):
    parser = parent.add_parser('food', help='food help')
    parser.set_defaults(func=root_handle)
    subparsers = parser.add_subparsers(help='subsub parser help')

    edit_register(subparsers)
    remove_register(subparsers)
    log_register(subparsers)
    import_register(subparsers)
    add_register(subparsers)

    # remove, add, edit, log
