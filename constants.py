import os

DIR = "/Users/svendcs/.bolognese/"
EXTENSION = '.yml'
CONFIG_PATH = os.path.join(DIR, 'config' + EXTENSION)
FOOD_DIR = os.path.join(DIR, 'food')
MEALS_DIR = os.path.join(DIR, 'meals')
EDITOR = os.environ.get('EDITOR','vim') #that easy!
