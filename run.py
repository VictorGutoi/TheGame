from display import screen_init, display
from player import Player
from world.square import *
from data_types import *

screen, fake_screen = screen_init(width, height)

player = Player(fake_screen)

test_square = Square(sqr_types[0], Pos((0, 0)))

squares = [test_square]

running = True
pygame.mouse.set_pos(0, 0)

while running:
    #    player.look_around(200, screen)

    running = display(screen, fake_screen, test_all, squares, player)
