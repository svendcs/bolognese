import constants
import os
import subprocess
import yaml
from dictionary_helpers import update_dictionary

defaults = {'carbs': 0, 'protein': 0, 'fat': 0, 'alcohol': 0}
def handle(args):
    vargs = vars(args)

    should_update = any(vargs[k] is not None for k in defaults.keys())

    if should_update:
        path = os.path.join(constants.DIR, 'config.yaml')
        with open(path, mode='r') as f:
            a = yaml.safe_load(f) or {}
        d = update_dictionary(defaults, a, vargs)
        with open(path, mode='w') as f:
            yaml.dump(d, f, default_flow_style=False)
    else:
        subprocess.call([constants.EDITOR, os.path.join(constants.DIR, 'config.yaml')])

def register(subparsers):
    parser = subparsers.add_parser('config', help='config help')
    parser.add_argument('--carbs', type=int, help='Set the number of carbs')
    parser.add_argument('--protein', type=int, help='Set the number of carbs')
    parser.add_argument('--fat', type=int, help='Set the number of carbs')
    parser.add_argument('--alcohol', type=int, help='Set the number of carbs')
    parser.set_defaults(func=handle)
