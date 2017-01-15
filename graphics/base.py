import os
import pygame

import config

all_sprites = pygame.sprite.LayeredUpdates()


class BaseSprite(pygame.sprite.Sprite):

    default_image = None
    image_path = NotImplemented
    group = NotImplemented
    ai_class = NotImplemented

    def __init__(self, start_x, start_y):
        pygame.sprite.Sprite.__init__(self, (all_sprites, self.group,))

        if self.__class__.default_image is None:
            full_image_path = os.path.join('images', self.image_path)
            self.__class__.default_image = pygame.image.load(full_image_path).convert_alpha()
        self.image = self.default_image
        self.rect = self.image.get_rect()
        self.x, self.y = start_x, start_y
        self.rect.center = self.x * config.TILE_SIZE, self.y * config.TILE_SIZE
        self.ai = self.ai_class()

    def update(self, frame_ms, ms_to_tick):
        self.sprite_update(frame_ms, ms_to_tick)
        if ms_to_tick <= 0:
            self.tick_update()

    def sprite_update(self, frame_ms, ms_to_tick):
        pass

    def tick_update(self):
        self.ai.progress()
