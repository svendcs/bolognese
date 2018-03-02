import os
import yaml

from bolognese.constants import DIARY_DIR, EXTENSION
from datetime import date
from bolognese.core.food_list import FoodList
from bolognese.core.servings import Servings

class Diary:
    def __init__(self, date: date):
        self.date = date
        self.foodlist = FoodList()

    def path(self):
        return os.path.join(DIARY_DIR, str(self.date) + EXTENSION)

    def exists(self):
        return os.path.isfile(self.path())

    def add_food(self, food, servings):
        self.foodlist.add_food(food.name, servings)

    def add_recipe(self, recipe, servings, recursive = False):
        if not recursive:
            self.foodlist.add_recipe(recipe.name, servings)
        else:
            factor = recipe.servings.get_factor(servings)
            for item in recipe.foodlist.items:
                serving = item['servings'] if 'servings' in item else 1
                new_serving = Servings.apply_factor(serving, factor)
                if 'food' in item:
                    self.foodlist.add_food(item['food'], new_serving)
                else:
                    self.foodlist.add_recipe(item['recipe'], new_serving)

    def update(self, items):
        assert(isinstance(items, list))
        self.foodlist.update(items)

    def load(self):
        with open(self.path(), mode='r') as f:
            self.foodlist.update(yaml.safe_load(f) or {})

    def save(self):
        with open(self.path(), mode='w') as f:
            yaml.dump(self.foodlist.items, f, default_flow_style=False, encoding='utf-8', allow_unicode=True)
