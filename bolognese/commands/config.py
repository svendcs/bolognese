import constants
import subprocess
from core.config import Config

def handle(args):
    vargs = vars(args)

    config = Config()

    if args.carbs is None and args.fat is None and args.protein is None and args.alcohol is None:
        subprocess.call([constants.EDITOR, config.path()])
    else:
        if config.exists():
            config.load()
        config.update(vargs)
        config.save()

def register(subparsers):
    parser = subparsers.add_parser('config', help='config help')
    parser.add_argument('--carbs', type=int, help='Set the number of carbs')
    parser.add_argument('--protein', type=int, help='Set the number of carbs')
    parser.add_argument('--fat', type=int, help='Set the number of carbs')
    parser.add_argument('--alcohol', type=int, help='Set the number of carbs')
    parser.set_defaults(func=handle)
