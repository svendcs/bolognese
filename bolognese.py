import argparse
import os
import sys
import constants
import commands.config

for folder in ['', 'food', 'meals', 'diary']:
    p = os.path.join(constants.DIR, folder)
    if os.path.exists(p):
        if not os.path.isdir(p):
            print("The location '{}' is not a directory".format(p))
    else:
        os.makedirs(p)

parser = argparse.ArgumentParser(prog='bolognese')
subparsers = parser.add_subparsers(help='sub-command help')

commands.config.register(subparsers)

args = parser.parse_args()
args.func(args)
