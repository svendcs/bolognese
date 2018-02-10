import re

class Servings:
    def __init__(self):
        self.rep = {'': 1}

    def __parse_rep(self, s):
        if isinstance(s, int):
            return "", s
        p = re.compile('(\d+)\s*([a-z]*)')
        m = p.search(s)
        return m.group(2), int(m.group(1))

    def update(self, l):
        assert(isinstance(l, list))
        for s in l:
            assert(isinstance(s, str) or isinstance(s, int))
            unit, amount = self.__parse_rep(s)
            self.rep[unit] = amount

    def get_factor(self, s):
        unit, amount = self.__parse_rep(s)
        assert unit in self.rep

        return amount / self.rep[unit]

    def to_list(self):
        res = []
        for unit, amount in self.rep.items():
            if unit == "":
                res.append(amount)
            else:
                res.append("{}{}".format(amount, unit))

        return res

    def is_valid_serving(self, s):
        unit, amount = self.__parse_rep(s)
        return unit in self.rep

