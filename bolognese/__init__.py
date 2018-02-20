import argparse
import os
import sys
import bolognese.constants
from bolognese.commands import food,config,meal,diary

def __handle(args):
    print("Root handle")

def main():
    for folder in ['', 'food', 'meals', 'diary']:
        p = os.path.join(constants.DIR, folder)
        if os.path.exists(p):
            if not os.path.isdir(p):
                print("The location '{}' is not a directory".format(p))
        else:
            os.makedirs(p)

    parser = argparse.ArgumentParser(prog='bolognese')
    subparsers = parser.add_subparsers(help='sub-command help')

    config.register(subparsers)
    food.register(subparsers)
    meal.register(subparsers)
    diary.register(subparsers)
    parser.set_defaults(func=__handle)

    args = parser.parse_args()
    args.func(args)
