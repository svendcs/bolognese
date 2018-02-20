import os
import constants
import yaml
from core.servings import Servings
from core.nutrients import Nutrients

class Food:
    def __init__(self, name):
        self.name = name
        self.nutrients = Nutrients()
        self.servings = Servings()

    def list():
        res = []
        for root, dirs, files in os.walk(constants.FOOD_DIR):
            for f in files:
                if root == constants.FOOD_DIR:
                    res.append(f)
                else:
                    res.append(root[len(constants.FOOD_DIR)+1:] + '/' + f)
        return res

    def path(self):
        return os.path.join(constants.FOOD_DIR, self.name + constants.EXTENSION)
    
    def exists(self):
        return os.path.isfile(self.path())

    def update(self, dic):
        if 'carbs' in dic.keys() and dic['carbs'] is not None:
            assert(isinstance(dic['carbs'], int))
            self.nutrients.carbs = dic['carbs']
        if 'protein' in dic.keys() and dic['protein'] is not None:
            assert(isinstance(dic['protein'], int))
            self.nutrients.protein = dic['protein']
        if 'fat' in dic.keys() and dic['fat'] is not None:
            assert(isinstance(dic['fat'], int))
            self.nutrients.fat = dic['fat']
        if 'alcohol' in dic.keys() and dic['alcohol'] is not None:
            assert(isinstance(dic['alcohol'], int))
            self.nutrients.alcohol = dic['alcohol']
        if 'servings' in dic.keys() and dic['servings'] is not None:
            self.servings.update(dic['servings'])

    def load(self):
        with open(self.path(), mode='r') as f:
            self.update(yaml.safe_load(f) or {})

    def save(self):
        with open(self.path(), mode='w') as f:
            dic = {
                'carbs': self.nutrients.carbs,
                'protein': self.nutrients.protein,
                'fat': self.nutrients.fat,
                'alcohol': self.nutrients.alcohol,
                'servings': self.servings.to_list(),
            }
            yaml.dump(dic, f, default_flow_style=False)

    def remove(self):
        os.remove(self.path())

