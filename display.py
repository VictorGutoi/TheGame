from pygame.locals import *
from run import player, squares
from world.square import *


# from player import Player

def screen_init(width, heigth):
    pygame.init()
    screen = pygame.display.set_mode((width, heigth), HWSURFACE | DOUBLEBUF | RESIZABLE)
    fake_screen = screen.copy()

    return screen, fake_screen


def display(screen, fake_screen):
    fake_screen.fill('black')
    _screen = screen

    print('a')
    test_all(squares, player)

    # image = pygame.image.load("/Users/victor/PycharmProjects/gameNewHouse/textures/test.jpg")  # self._type.image)
    # fake_screen.blit(image, (0, 0))

    _screen.blit(pygame.transform.scale(fake_screen, _screen.get_rect().size), (0, 0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            return False
        elif event.type == VIDEORESIZE:
            _screen = pygame.display.set_mode(event.size, HWSURFACE | DOUBLEBUF | RESIZABLE)

    return True
