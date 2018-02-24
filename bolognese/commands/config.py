import subprocess

from bolognese.constants import EDITOR
from bolognese.core.config import Config
from bolognese.core.nutrients import Nutrients

def handle(args):
    vargs = vars(args)
    config = Config()

    if all(vargs[nutr] is None for nutr in Nutrients.NUTRIENTS):
        subprocess.call([EDITOR, config.path()])
    else:
        if config.exists():
            config.load()
        config.update(vargs)
        config.save()

def register(subparsers):
    parser = subparsers.add_parser('config', help='config help')
    for nutr in Nutrients.NUTRIENTS:
        parser.add_argument('--{}'.format(nutr), type=float, help='Set the number of {}'.format(nutr))
    parser.set_defaults(func=handle)

