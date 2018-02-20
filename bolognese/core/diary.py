import os
import yaml

from bolognese.constants import DIARY_DIR, EXTENSION
from datetime import date
from bolognese.core.food_list import FoodList

class Diary:
    def __init__(self, date: date):
        self.date = date
        self.foodlist = FoodList()

    def path(self):
        return os.path.join(DIARY_DIR, str(self.date) + EXTENSION)

    def exists(self):
        return os.path.isfile(self.path())

    def add_food(self, food, servings):
        self.foodlist.add_food(food, servings)

    def add_meal(self, meal, servings):
        self.foodlist.add_meal(meal, servings)

    def update(self, items):
        assert(isinstance(items, list))
        self.foodlist.update(items)

    def load(self):
        with open(self.path(), mode='r') as f:
            self.foodlist.update(yaml.safe_load(f) or {})

    def save(self):
        with open(self.path(), mode='w') as f:
            yaml.dump(self.foodlist.items, f, default_flow_style=False)
