class FoodList:
    def __init__(self):
        self.items = []

    def add_food(self, food, servings):
        self.items.append({'food': food, 'servings': servings})

    def add_recipe(self, recipe, servings):
        self.items.append({'recipe': recipe, 'servings': servings})

    def update(self, items):
        assert(isinstance(items, list))
        for item in items:
            assert(isinstance(item, dict))
            assert('servings' not in item or isinstance(item['servings'], str) or isinstance(item['servings'], int))

            t = 'food' if 'food' in item else 'recipe'
            assert(t in item)
            assert(isinstance(item[t], str))
            self.items.append({t: item[t], 'servings': item['servings'] if 'servings' in item else 1})
