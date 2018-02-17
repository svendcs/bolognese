class Nutrients:
    def __init__(self):
        self.carbs = 0
        self.alcohol = 0
        self.fat = 0
        self.protein = 0

    def __str__(self):
        return "(carbs: {}, protein: {}, fat: {}, alcohol: {})".format(self.carbs, self.protein, self.fat, self.alcohol)

    def __add__(a, b):
        c = Nutrients()
        c.carbs = a.carbs + b.carbs
        c.fat = a.fat + b.fat
        c.alcohol = a.alcohol + b.alcohol
        c.protein = a.protein + b.protein
        return c

    def __rmul__(self, k):
        c = Nutrients()
        c.carbs = k * self.carbs
        c.fat = k * self.fat
        c.protein = k * self.protein
        c.alcohol = k * self.alcohol
        return c