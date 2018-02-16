import os
import constants
import yaml
from datetime import date

class Diary:
    def __init__(self, date: date):
        self.date = date
        self.items = []

    def path(self):
        return os.path.join(constants.DIARY_DIR, str(self.date) + constants.EXTENSION)

    def exists(self):
        return os.path.isfile(self.path())

    def add_food(self, food, servings):
        self.items.append({'food': food, 'servings': servings})

    def add_meal(self, meal, servings):
        self.items.append({'meal': meal, 'servings': servings})

    def update(self, items):
        assert(isinstance(items, list))
        for item in items:
            assert(isinstance(item, dict))
            assert('servings' not in item or isinstance(item['servings'], str) or isinstance(item['servings'], int))

            t = 'food' if 'food' in item else 'meal'
            assert(t in item)
            assert(isinstance(item[t], str))
            self.items.append({t: item[t], 'servings': item['servings'] if 'servings' in item else 1})

    def load(self):
        with open(self.path(), mode='r') as f:
            self.update(yaml.safe_load(f) or {})

    def save(self):
        with open(self.path(), mode='w') as f:
            yaml.dump(self.items, f, default_flow_style=False)
