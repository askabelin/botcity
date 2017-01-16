import os
import pygame

import config
from graphic.base import BaseSprite
from logic.field import FieldAI, MATURE_STATE


class Field(BaseSprite):

    ai_class = FieldAI
    group = pygame.sprite.Group()
    image_mature = None
    image_path = 'terrain/field.png'
    image_path_mature = 'terrain/field_mature.png'

    def __init__(self, *args, **kwargs):
        super(Field, self).__init__(*args, **kwargs)
        self.current_image = self.image
        if self.__class__.image_mature is None:
            path = os.path.join('images', self.image_path_mature)
            self.__class__.image_mature = pygame.image.load(path).convert()

    def tick_update(self):
        self.ai.progress()
        if MATURE_STATE in self.ai.states and self.current_image != self.image_mature:
            self.image = self.image_mature
            self.rect = self.current_image.get_rect()
            self.rect.center = self.x * config.TILE_SIZE, self.y * config.TILE_SIZE
