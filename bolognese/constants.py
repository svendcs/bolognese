import os

DIR = os.path.expanduser("~/.config/bolognese")
EXTENSION = '.yml'
FOOD_DIR = os.path.join(DIR, 'food')
MEALS_DIR = os.path.join(DIR, 'meals')
DIARY_DIR = os.path.join(DIR, 'diary')
EDITOR = os.environ.get('EDITOR','vim')
