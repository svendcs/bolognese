import os
import constants
import yaml
import servings
from servings import Servings

class Meal:
    def __init__(self, name):
        self.name = name
        self.foods = []
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
        if 'foods' in dic.keys():
            assert(isinstance(dic['foods'], list))
            for item in dic['foods']:
                assert(isinstance(item, dict))
                assert('food' in item and isinstance(item['food'], str))
                assert('servings' not in item or isinstance(item['servings'], str) or isinstance(item['servings'], int))

                self.foods.append({'food': item['food'], 'servings': item['servings'] if 'servings' in item else 1})

    def add_food(self, food, servings):
        self.foods.append({'food': food, 'servings': servings})

    def load(self):
        with open(self.path(), mode='r') as f:
            self.update(yaml.safe_load(f) or {})

    def save(self):
        with open(self.path(), mode='w') as f:
            dic = {
                'foods': self.foods,
                'servings': self.servings.to_list(),
            }
            yaml.dump(dic, f, default_flow_style=False)

