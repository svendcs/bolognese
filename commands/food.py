import constants
import os
import sys
import subprocess
import yaml
from dictionary_helpers import update_dictionary

defaults = {'carbs': 0, 'protein': 0, 'fat': 0, 'alcohol': 0, 'servings': []}

def food_path(food):
    return os.path.join(constants.FOOD_DIR, food + constants.EXTENSION)

def root_handle(args):
    for root, dirs, files in os.walk(constants.FOOD_DIR):
        for f in files:
            if root == constants.FOOD_DIR:
                print(f)
            else:
                print(root[len(constants.FOOD_DIR)+1:] + '/' + f)

def edit_handle(args):
    path = food_path(args.food)
    vargs = vars(args)

    if not os.path.isfile(path):
        print("The food '{}' does not exist.".format(args.food), file=sys.stderr)
        return

    should_update = any(vargs[k] is not None for k in defaults.keys())
    if should_update:
        with open(constants.CONFIG_PATH, mode='r') as f:
            a = yaml.safe_load(f) or {}
        d = update_dictionary(defaults, a, vargs)
        with open(constants.CONFIG_PATH, mode='w') as f:
            yaml.dump(d, f, default_flow_style=False)
    else:
        subprocess.call([constants.EDITOR, constants.CONFIG_PATH])

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
    path = food_path(args.food)
    vargs = vars(args)

    if os.path.exists(path):
        print("The food '{}' already exists.".format(args.food), file=sys.stderr)
        return

    should_update = any(vargs[k] is not None for k in defaults.keys())
    if should_update:
        with open(constants.CONFIG_PATH, mode='r') as f:
            a = yaml.safe_load(f) or {}
        d = update_dictionary(defaults, a, vargs)
        with open(constants.CONFIG_PATH, mode='w') as f:
            yaml.dump(d, f, default_flow_style=False)
    else:
        subprocess.call([constants.EDITOR, constants.CONFIG_PATH])

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
    log_parser.add_argument('--carbs', type=int, help='Set the number of foo')
    log_parser.add_argument('--protein', type=int, help='Set the number of foo')
    log_parser.add_argument('--fat', type=int, help='Set the number of foo')
    log_parser.add_argument('--alcohol', type=int, help='Set the number of foo')
    log_parser.add_argument('--servings', type=str, nargs='+', help='Set the number of foo')

def remove_handle(args):
    path = food_path(args.food)

    if not os.path.isfile(path):
        print("The food '{}' does not exist.".format(args.food), file=sys.stderr)
    else:
        os.remove(path)

def remove_register(parent):
    remove_parser = parent.add_parser('remove')
    remove_parser.set_defaults(func=remove_handle)
    remove_parser.add_argument('food', type=str, help='Set the number of foo')

def import_handle(args):
    print("Import handler")

def import_register(parent):
    import_parser = parent.add_parser('import')
    import_parser.set_defaults(func=import_handle)
    import_parser.add_argument('food', type=str, help='Set the number of foo')
    import_parser.add_argument('--carbs', type=int, help='Set the number of foo')
    import_parser.add_argument('--protein', type=int, help='Set the number of foo')
    import_parser.add_argument('--fat', type=int, help='Set the number of foo')
    import_parser.add_argument('--alcohol', type=int, help='Set the number of foo')
    import_parser.add_argument('--servings', type=str, nargs='+', help='Set the number of foo')

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
