import os

DIR = os.path.expanduser("~/.config/bolognese")
EXTENSION = '.yml'
FOOD_DIR = os.path.join(DIR, 'food')
RECIPES_DIR = os.path.join(DIR, 'recipes')
DIARY_DIR = os.path.join(DIR, 'diary')
EDITOR = os.environ.get('EDITOR','vim')
