import sys
import subprocess

from bolognese.constants import EDITOR
from bolognese.core.food import Food
from bolognese.core.serving import Serving
from bolognese.core.nutrients import Nutrients

def root_handle(args):
    pass

def edit_handle(args):
    food = Food(args.food)
    vargs = vars(args)

    if all(vargs[nutr] is None for nutr in Nutrients.NUTRIENTS) and args.servings is None:
        subprocess.call([EDITOR, food.path()])
    else:
        if food.exists():
            food.load()
        food.update(vargs)
        food.save()

def edit_register(parent):
    parser = parent.add_parser('edit')
    parser.add_argument('food', type=str, help='Set the number of foo')
    for nutr in Nutrients.NUTRIENTS:
        parser.add_argument('--{}'.format(nutr), type=float, help='Set the number of {}'.format(nutr))
    parser.set_defaults(func=edit_handle)
    parser.add_argument('--servings', type=str, nargs='+', help='Set the number of foo')

def add_handle(args):
    food = Food(args.food)
    vargs = vars(args)

    if food.exists():
        print("The food '{}' already exists.".format(args.food), file=sys.stderr)
        return

    if all(vargs[nutr] is None for nutr in Nutrients.NUTRIENTS) and args.servings is None:
        food.save() # First create the new file
        subprocess.call([EDITOR, food.path()])
    else:
        food.update(vargs)
        food.save()

def add_register(parent):
    parser = parent.add_parser('add')
    parser.set_defaults(func=add_handle)
    parser.add_argument('food', type=str, help='Set the number of foo')
    for nutr in Nutrients.NUTRIENTS:
        parser.add_argument('--{}'.format(nutr), type=float, help='Set the number of {}'.format(nutr))
    parser.add_argument('--servings', type=str, nargs='+', help='Set the number of foo')

def copy_handle(args):
    food = Food(args.food)
    new_food = Food(args.new_name)

    if not food.exists():
        print("The food '{}' does not exist.".format(args.food), file=sys.stderr)
        return

    if new_food.exists():
        print("The food '{}' already exists.".format(args.new_name), file=sys.stderr)
        return

    food.load()
    food.name = args.new_name
    food.save()

def copy_register(parent):
    remove_parser = parent.add_parser('copy')
    remove_parser.set_defaults(func=copy_handle)
    remove_parser.add_argument('food', type=str, help='Set the number of foo')
    remove_parser.add_argument('new_name', type=str, help='Set the number of foo')

def move_handle(args):
    food = Food(args.food)
    new_food = Food(args.new_name)

    if not food.exists():
        print("The food '{}' does not exist.".format(args.food), file=sys.stderr)
        return

    if new_food.exists():
        print("The food '{}' already exists.".format(args.new_name), file=sys.stderr)
        return

    food.load()
    food.remove()
    food.name = args.new_name
    food.save()

def move_register(parent):
    remove_parser = parent.add_parser('move')
    remove_parser.set_defaults(func=move_handle)
    remove_parser.add_argument('food', type=str, help='Set the number of foo')
    remove_parser.add_argument('new_name', type=str, help='Set the number of foo')

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
    from bolognese.databases.fooddata import Fooddata

    food = Food(args.food)
    if food.exists():
        print("The food '{}' already exists.".format(args.food), file=sys.stderr)
        return

    food = Fooddata.get_food(args.food, args.food_id)

    food.save()

def import_register(parent):
    import_parser = parent.add_parser('import')
    import_parser.set_defaults(func=import_handle)
    # import_parser.add_argument('database', type=str, choices=['fooddata'], help='Set the number of foo')
    import_parser.add_argument('food', type=str, help='Set the number of foo')
    import_parser.add_argument('food_id', type=str, help='Set the number of foo')

def list_handle(args):
    for f in Food.list():
        print(f)

def list_register(parent):
    import_parser = parent.add_parser('list')
    import_parser.set_defaults(func=list_handle)

def register(parent):
    parser = parent.add_parser('food', help='food help')
    subparsers = parser.add_subparsers(help='subsub parser help')

    edit_register(subparsers)
    copy_register(subparsers)
    move_register(subparsers)
    remove_register(subparsers)
    import_register(subparsers)
    list_register(subparsers)
    add_register(subparsers)

