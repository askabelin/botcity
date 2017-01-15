import pygame

import config
from graphics.utils import get_image_grid

D_DIRECTION = 'd'
L_DIRECTION = 'l'
R_DIRECTION = 'r'
U_DIRECTION = 'u'
DIRECTION_MAP = {D_DIRECTION: 0, L_DIRECTION: 1, R_DIRECTION: 2, U_DIRECTION: 3}


class Villager(pygame.sprite.Sprite):

    images = None

    def __init__(self, start_x, start_y, groups):
        pygame.sprite.Sprite.__init__(self, groups)
        self.direction = D_DIRECTION
        if self.__class__.images is None:
            self.__class__.images = get_image_grid('images/sprites/villager.png', 16)

        self.rect = self.image.get_rect()
        self.x = start_x
        self.y = start_y
        self.update()

    @property
    def image(self):
        return self.images[0][DIRECTION_MAP[self.direction]]

    def update(self):
        self.rect.centerx = self.x * config.TILE_SIZE
        self.rect.centery = self.y * config.TILE_SIZE

    def move_down(self):
        self.y += 1
        self.direction = D_DIRECTION

    def move_up(self):
        self.y -= 1
        self.direction = U_DIRECTION

    def move_left(self):
        self.x -= 1
        self.direction = L_DIRECTION

    def move_right(self):
        self.x += 1
        self.direction = R_DIRECTION
