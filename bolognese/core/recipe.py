import os
import yaml

from bolognese.constants import RECIPES_DIR, EXTENSION
from bolognese.core.serving import Serving
from bolognese.core.serving_list import ServingList
from bolognese.core.food_list import FoodList

class Recipe:
    def __init__(self, name):
        self.name = name
        self.food_list = FoodList()
        self.servings = ServingList()

    def list():
        res = []
        for root, dirs, files in os.walk(RECIPES_DIR):
            for f in files:
                if root == RECIPES_DIR:
                    p = f
                else:
                    p = root[len(RECIPES_DIR)+1:] + '/' + f
                res.append(os.path.splitext(p)[0])
        return res

    def path(self):
        return os.path.join(RECIPES_DIR, self.name + EXTENSION)

    def exists(self):
        return os.path.isfile(self.path())

    def update(self, dic):
        if 'servings' in dic.keys() and dic['servings'] is not None:
            self.servings.update(dic['servings'])
        if 'items' in dic.keys():
            self.food_list.update(dic['items'])

    def add_food(self, food, serving):
        self.food_list.add_food(food, serving)

    def add_recipe(self, recipe, serving):
        self.food_list.add_recipe(recipe, serving)

    def load(self):
        with open(self.path(), mode='r') as f:
            self.update(yaml.safe_load(f) or {})

    def remove(self):
        os.remove(self.path())

    def save(self):
        os.makedirs(os.path.dirname(self.path()), exist_ok = True)
        with open(self.path(), mode='w') as f:
            dic = {
                'items': self.food_list.items,
                'servings': list(map(str, self.servings))
            }
            yaml.dump(dic, f, default_flow_style=False, encoding='utf-8', allow_unicode=True)

