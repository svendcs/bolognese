import os

DIR = "/Users/svendcs/.bolognese/"
EXTENSION = '.yml'
CONFIG_PATH = os.path.join(DIR, 'config' + EXTENSION)
FOOD_DIR = os.path.join(DIR, 'food')
MEALS_DIR = os.path.join(DIR, 'meals')
DIARY_DIR = os.path.join(DIR, 'diary')
EDITOR = os.environ.get('EDITOR','vim')
