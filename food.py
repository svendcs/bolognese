import os
import constants
import yaml
import servings
from servings import Servings

class Food:
    def __init__(self, name):
        self.name = name
        self.carbs = 0
        self.protein = 0
        self.fat = 0
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
            self.carbs = dic['carbs']
        if 'protein' in dic.keys() and dic['protein'] is not None:
            self.protein = dic['protein'] 
        if 'fat' in dic.keys() and dic['fat'] is not None:
            self.fat = dic['fat']
        if 'alcohol' in dic.keys() and dic['alcohol'] is not None:
            self.alcohol = dic['alcohol']
        if 'servings' in dic.keys() and dic['servings'] is not None:
            self.servings.update(dic['servings'])

    def load(self):
        with open(self.path(), mode='r') as f:
            self.update(yaml.safe_load(f) or {})

    def save(self):
        with open(self.path(), mode='w') as f:
            dic = {
                'carbs': self.carbs,
                'protein': self.protein,
                'fat': self.fat,
                'alcohol': self.alcohol,
                'servings': self.servings.to_list(),
            }
            yaml.dump(dic, f, default_flow_style=False)

    def remove(self):
        os.remove(self.path())

