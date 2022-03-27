import pygame
from data_types import *


class Square_Type:
    def __init__(self, image, square_type):
        self.type = square_type
        self.image = image


class Square:
    def __init__(self, _type, pos, angle=None):
        self._type: Square_Type = _type
        self.angle = angle

        if type(pos) == Pos:
            self.pos = pos
        else:
            self.pos = Pos(pos)

        if type(self._type) != Square_Type:
            print(1 + "2")

    def draw(self, player, r, angle, fake_screen):
        # Obtain angle from d - 45 to position cat
        _angle = angle + 45 - player.direction

        part_of_segment = 90 / _angle

        image = pygame.image.load("/Users/victor/PycharmProjects/gameNewHouse/textures/test.jpg")  # self._type.image)
        fake_screen.blit(image, (self.pos.x, self.pos.y))


test1 = Square_Type("/Users/victor/PycharmProjects/gameNewHouse/textures/test.jpg", "test_1")
sqr_types = [
    test1
]


def test_all(squares, player):
    for x in squares:
        player.in_bounds(16, x.pos, x)
