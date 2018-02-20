import os
import constants
import yaml
from core.nutrients import Nutrients

class Config:
    def __init__(self):
        self.nutrients = Nutrients()

    def path(self):
        return os.path.join(constants.DIR, 'config' + constants.EXTENSION)

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
            }
            yaml.dump(dic, f, default_flow_style=False)

