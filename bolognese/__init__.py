import argparse
import os
import sys
import bolognese.constants
from bolognese.commands import food,config,recipe,diary

def __handle(args):
    print("Root handle")

def main():
    parser = argparse.ArgumentParser(prog='bolognese')
    subparsers = parser.add_subparsers(help='sub-command help')

    config.register(subparsers)
    food.register(subparsers)
    recipe.register(subparsers)
    diary.register(subparsers)
    parser.set_defaults(func=__handle)

    args = parser.parse_args()
    args.func(args)
