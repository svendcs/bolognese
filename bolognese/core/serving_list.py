from bolognese.constants import RECIPES_DIR, EXTENSION
from bolognese.core.serving import Serving

class ServingList:
    def __init__(self):
        self.servings = []

    def update(self, l):
        new_servings = [Serving.from_string(s) for s in l]
        for serving in self.servings:
            if any(serving.compatible(other) for other in new_servings):
                continue
            new_servings.append(serving)
        self.servings = new_servings

    def compatible(self, serving):
        return any(serving.compatible(other) for other in self.servings)

    def get_factor(self, serving):
        for other in self.servings:
            if not serving.compatible(other):
                continue
            return serving / other
        raise Exception("Tried to get factor of non-compatible serving to serving list.")

