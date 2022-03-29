import math

width, height = 1440, 875


class Pos:
    def __init__(self, x_y):
        self.x, self.y = x_y


def pitagora(l1, l2):
    return math.sqrt(l1 ** 2 + l2 ** 2)
