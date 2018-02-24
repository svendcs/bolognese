import os
import yaml

from bolognese.constants import DIR, EXTENSION
from bolognese.core.nutrients import Nutrients

class Config:
    def __init__(self):
        self.nutrients = Nutrients()

    def path(self):
        return os.path.join(DIR, 'config' + EXTENSION)

    def exists(self):
        return os.path.isfile(self.path())

    def update(self, dic):
        self.nutrients.update(dic)

    def load(self):
        with open(self.path(), mode='r') as f:
            self.update(yaml.safe_load(f) or {})

    def save(self):
        with open(self.path(), mode='w') as f:
            yaml.dump(self.nutrients.dic, f, default_flow_style=False)

