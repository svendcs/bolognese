import re

class Servings:
    def __init__(self):
        self.rep = {'': 1}

    def __parse_rep(self, s):
        p = re.compile('(\d+(\.\d+)?)\s*([a-z]*)')
        m = p.search(str(s))
        return m.group(3), float(m.group(1))

    def update(self, l):
        assert(isinstance(l, list))
        for s in l:
            unit, amount = self.__parse_rep(s)
            self.rep[unit] = amount

    def get_factor(self, s):
        unit, amount = self.__parse_rep(s)
        assert unit in self.rep

        return amount / self.rep[unit]

    def __iter__(self):
        res = []
        for unit, amount in self.rep.items():
            if unit == "":
                yield amount
            else:
                yield "{}{}".format(amount, unit)

    def is_valid_serving(self, s):
        unit, amount = self.__parse_rep(s)
        return unit in self.rep

