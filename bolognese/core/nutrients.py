class Nutrients:
    NUTRIENTS = ['carbs', 'protein', 'fat', 'saturated_fat', 'alcohol', 'sugar', 'fiber', 'sodium']

    def __init__(self):
        self.dic = {}
        for nutr in Nutrients.NUTRIENTS:
            self.dic[nutr] = 0.0

    def items(self):
        return self.dic.items()

    def __str__(self):
        return str(self.dic)

    def __add__(a, b):
        c = Nutrients()
        for nutr in Nutrients.NUTRIENTS:
            c[nutr] = a[nutr] + b[nutr]
        return c

    def __sub__(a, b):
        c = Nutrients()
        for nutr in Nutrients.NUTRIENTS:
            c[nutr] = a[nutr] - b[nutr]
        return c

    def __getitem__(self, key):
        return self.dic[key]

    def __setitem__(self, key, v:float):
        if not key in Nutrients.NUTRIENTS:
            raise KeyError()
        self.dic[key] = v

    def __rmul__(self, k):
        c = Nutrients()
        for nutr in Nutrients.NUTRIENTS:
            c[nutr] = k * self.dic[nutr]
        return c

    def update(self, dic):
        for nutr in Nutrients.NUTRIENTS:
            if nutr in dic.keys() and dic[nutr] is not None:
                self.dic[nutr] = float(dic[nutr])

    @property
    def kilocalories(self):
        return self.kilojoule * 0.239

    @property
    def kilojoule(self):
        return self['carbs'] * 17 + self['fat'] * 38 + self['protein'] * 17 + self['alcohol'] * 29

