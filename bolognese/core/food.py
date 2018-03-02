import os
import yaml

from bolognese.constants import FOOD_DIR, EXTENSION
from bolognese.core.servings import Servings
from bolognese.core.nutrients import Nutrients

class Food:
    def __init__(self, name):
        self.name = name
        self.nutrients = Nutrients()
        self.servings = Servings()

    def __str__(self):
        return "{}: {}".format(self.name, self.nutrients)

    def list():
        res = []
        for root, dirs, files in os.walk(FOOD_DIR):
            for f in files:
                if root == FOOD_DIR:
                    p = f
                else:
                    p = root[len(FOOD_DIR)+1:] + '/' + f

                res.append(os.path.splitext(p)[0])
        return res

    def path(self):
        return os.path.join(FOOD_DIR, self.name + EXTENSION)

    def exists(self):
        return os.path.isfile(self.path())

    def update(self, dic):
        self.nutrients.update(dic)
        if 'servings' in dic.keys() and dic['servings'] is not None:
            self.servings.update(dic['servings'])

    def load(self):
        with open(self.path(), mode='r') as f:
            self.update(yaml.safe_load(f) or {})

    def save(self):
        os.makedirs(os.path.dirname(self.path()), exist_ok = True)
        with open(self.path(), mode='w') as f:
            dic = {
                'servings':  list(self.servings),
                **self.nutrients.dic
            }
            yaml.dump(dic, f, default_flow_style=False)

    def remove(self):
        os.remove(self.path())

