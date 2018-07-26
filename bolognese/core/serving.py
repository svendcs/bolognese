import re

class ServingException(Exception):
    def __init__(self, val):
        self.message = 'The value "{}" is not a correct serving'.format(val)

class IncompatibleServingException(Exception):
    def __init__(self, a, b):
        self.message = 'The servings "{}" and "{}" and not compatible.'.format(a,b)

class Serving:
    def __init__(self, unit, amount):
        self.unit = unit
        self.amount = amount

    def from_string(s):
        p = re.compile('^(\d+(\.\d+)?)\s*([a-z]*)$')
        m = p.search(str(s))
        if m is None:
            raise ServingException(str(s))

        unit = m.group(3)
        amount = float(m.group(1))
        return Serving(unit, amount)

    def compatible(self, other):
        return self.unit == other.unit

    def __truediv__(self, s):
        if not self.compatible(s):
            raise IncompatibleServingException(self, s)
        return self.amount / s.amount

    def __rmul__(self, k):
        return Serving(self.unit, self.amount*k)

    def __str__(self):
        return "{}{}".format(self.amount,self.unit)
