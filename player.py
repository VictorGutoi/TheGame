import pygame
from data_types import *


class Player:
    def __init__(self, fake_screen):
        self.pos = Pos((1, 0))
        self.direction = 0  # Degrees

        self.m_pos = pygame.mouse.get_pos()
        self.fake_screen = fake_screen

    def in_bounds(self, r, pos, square):
        lefter = False

        if pitagora(pos.x - self.pos.x, pos.y - self.pos.y) <= r:
            add_on = 0
            if pos.x < self.pos.x:
                add_on = 180

            verify_min = self.direction - 180
            verify_max = self.direction + 45

            angle = 0 + add_on
            if angle >= 360 or angle <= -360:
                angle = round(angle / 360) - 1

            if pos.x - self.pos.x == 0 or pos.y - self.pos.y == 0:
                if pos.y - self.pos.y == 0:
                    angle = 90 + add_on

                if verify_min <= angle <= verify_max:
                    square.draw(self, 16, angle, pitagora(pos.x - self.pos.x, pos.y - self.pos.y),
                                self.direction, self.fake_screen)

            else:
                angle = math.degrees(math.atan(math.sqrt((pos.x - self.pos.x) ** 2) /
                                               math.sqrt((pos.y - self.pos.y) ** 2))) + add_on
                if verify_min <= angle <= verify_max:
                    square.draw(self, 16, angle, pitagora(pos.x - self.pos.x, pos.y - self.pos.y),
                                self.direction, self.fake_screen)
            print(angle, self.direction, self.direction - 45, self.direction + 45)

    def correct_direction(self):
        if self.direction > 360:
            self.direction = 0
        if self.direction < 0:
            self.direction = 360

    def look_around(self):
        x, y = pygame.mouse.get_pos()
        x2, y2 = self.m_pos
        if x < x2:
            self.direction -= width / 360
        elif x > x2:
            self.direction += width / 360

        self.correct_direction()

        self.m_pos = pygame.mouse.get_pos()
