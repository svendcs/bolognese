from bolognese.core.serving import Serving

class FoodList:
    def __init__(self):
        self.items = []

    def add_food(self, food, serving):
        self.items.append({'food': food.name, 'serving': str(serving)})

    def add_recipe(self, recipe, serving):
        self.items.append({'recipe': recipe.name, 'serving': str(serving)})

    def update(self, items):
        if not isinstance(items, list):
            raise Exception('The loaded food list is not a list.')

        for item in items:
            if not isinstance(item, dict):
                raise Exception('The loaded food list contains an invalid item.')
            serving = Serving.from_string(item['serving'] if 'serving' in item else '1')

            if not ('food' in item or 'recipe' in item):
                raise Exception('The loaded food list contains an invalid item.')

            if 'food' in item:
                self.items.append({'food': item['food'], 'serving': str(serving)})
            else:
                self.items.append({'recipe': item['serving'], 'serving': str(serving)})

