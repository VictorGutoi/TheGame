import pygame
from data_types import *


class Player:
    def __init__(self, fake_screen):
        self.pos = Pos((-1, -1))
        self.direction = 0  # Degrees

        self.m_pos = pygame.mouse.get_pos()
        self.fake_screen = fake_screen

    def in_bounds(self, r, pos, square):
        if pitagora(pos.x - self.pos.x, pos.y - self.pos.y) <= r:
            add_on = 0
            if pos.x < self.pos.x:
                add_on = 180

            if pos.x - self.pos.x == 0 or pos.y - self.pos.y == 0:
                angle = 0 + add_on
                if pos.y - self.pos.y == 0:
                    angle = 90 + add_on

                if self.direction - 45 <= angle <= self.direction + 45:
                    square.draw(self, 16, angle, pitagora(pos.x - self.pos.x, pos.y - self.pos.y), self.fake_screen)

            else:
                angle = math.degrees(math.atan(math.sqrt((pos.x - self.pos.x) ** 2) / math.sqrt((pos.y - self.pos.y) ** 2))) + add_on
                if self.direction - 45 <= angle <= self.direction + 45:
                    square.draw(self, 16, angle, pitagora(pos.x - self.pos.x, pos.y - self.pos.y), self.fake_screen)

    # def look_around(self, screen_width):
    #     x, y = pygame.mouse.get_pos()
    #     x2, y2 = self.m_pos
    #     if x < x2:
    #         self.direction -= screen_width / 360
    #     elif x > x2:
    #         self.direction += screen_width / 360
    #
    #     self.m_pos = pygame.mouse.get_pos()
