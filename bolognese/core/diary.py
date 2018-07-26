import os
import yaml

from bolognese.constants import DIARY_DIR, EXTENSION
from datetime import date
from bolognese.core.food_list import FoodList
from bolognese.core.food import Food
from bolognese.core.recipe import Recipe
from bolognese.core.serving import Serving

class Diary:
    def __init__(self, date: date):
        self.date = date
        self.food_list = FoodList()

    def path(self):
        return os.path.join(DIARY_DIR, str(self.date) + EXTENSION)

    def exists(self):
        return os.path.isfile(self.path())

    def add_food(self, food, serving):
        self.food_list.add_food(food, serving)

    def add_recipe(self, recipe, serving, recursive = False):
        if not recursive:
            self.food_list.add_recipe(recipe, serving)
        else:
            factor = recipe.servings.get_factor(serving)
            for item in recipe.food_list.items:
                serving = Serving.from_string(item['serving']) if 'serving' in item else Serving('', 1)
                new_serving = factor * serving
                print(serving, new_serving)
                if 'food' in item:
                    self.food_list.add_food(Food(item['food']), new_serving)
                else:
                    self.food_list.add_recipe(Recipe(item['recipe']), new_serving)

    def update(self, items):
        assert(isinstance(items, list))
        self.food_list.update(items)

    def load(self):
        with open(self.path(), mode='r') as f:
            self.food_list.update(yaml.safe_load(f) or [])

    def save(self):
        with open(self.path(), mode='w') as f:
            yaml.dump(self.food_list.items, f, default_flow_style=False, encoding='utf-8', allow_unicode=True)
