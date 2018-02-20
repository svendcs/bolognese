import os
import constants
import yaml
from core.servings import Servings
from core.food_list import FoodList

class Meal:
    def __init__(self, name):
        self.name = name
        self.foodlist = FoodList()
        self.servings = Servings()

    def list():
        res = []
        for root, dirs, files in os.walk(constants.MEALS_DIR):
            for f in files:
                if root == constants.MEALS_DIR:
                    res.append(f)
                else:
                    res.append(root[len(constants.MEALS_DIR)+1:] + '/' + f)
        return res

    def path(self):
        return os.path.join(constants.MEALS_DIR, self.name + constants.EXTENSION)
    
    def exists(self):
        return os.path.isfile(self.path())

    def update(self, dic):
        if 'servings' in dic.keys() and dic['servings'] is not None:
            self.servings.update(dic['servings'])
        if 'items' in dic.keys():
            self.foodlist.update(dic['items'])

    def add_food(self, food, servings):
        self.foodlist.add_food(food, servings)

    def add_meal(self, meal, servings):
        self.foodlist.add_meal(meal, servings)

    def load(self):
        with open(self.path(), mode='r') as f:
            self.update(yaml.safe_load(f) or {})

    def save(self):
        with open(self.path(), mode='w') as f:
            dic = {
                'items': self.foodlist.items,
                'servings': self.servings.to_list(),
            }
            yaml.dump(dic, f, default_flow_style=False)

