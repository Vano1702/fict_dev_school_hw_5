class Vector:
    def __init__(self, elements):
        self.elements = elements

    def __str__(self):
        res = '('
        for i in range(len(self.elements)): res += str(self.elements[i]) + ","
        return res[:-1] + ")"

    def equals(self, vect):
        return True if self.elements == vect.elements else False

    def add(self, vect):
        if len(vect.elements) == len(self.elements):
            addend = vect.elements
            sum = [self.elements[i] + addend[i] for i in range(0, len(addend))]
            return Vector(sum)
        else:
            raise Exception("You are trying to add vectors with different lengths!")

    def subtract(self, vect):
        if len(vect.elements) == len(self.elements):
            subtrahend = vect.elements
            dif = [self.elements[i] - subtrahend[i] for i in range(0, len(subtrahend))]
            return Vector(dif)
        else:
            raise Exception("You are trying to subtract vectors with different lengths!")

    def dot(self, vect):
        if len(vect.elements) == len(self.elements):
            factor = vect.elements
            res = 0
            for i in range(len(factor)): res += self.elements[i] * factor[i]
            return res
        else:
            raise Exception("You are trying to dot vectors with different lengths!")

    def norm(self):
        res = 0
        for i in range(len(self.elements)): res += self.elements[i]**2
        return res ** 0.5
