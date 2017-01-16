import pygame

import config
from graphic.base import BaseSprite
from graphic.field import Field
from logic.man import ManAI, MOVE_D, MOVE_U, MOVE_R, MOVE_L, BUILD_FIELD


class BaseMan(BaseSprite):
    group = pygame.sprite.Group()
    ai_class = ManAI
    _layer = 5

    def __init__(self, *args, **kwargs):
        super(BaseMan, self).__init__(*args, **kwargs)
        self.target_x, self.target_y = self.x, self.y
        self.target_x_px, self.target_y_px = self.rect.center

    def sprite_update(self, frame_ms, ms_to_tick):
        if ms_to_tick:
            if self.rect.centerx != self.target_x_px:
                dist_x = self.target_x_px - self.rect.centerx
                delta_x = dist_x / (float(ms_to_tick) + frame_ms) * frame_ms
                self.rect.centerx += delta_x
            elif self.rect.centery != self.target_y_px:
                dist_y = self.target_y_px - self.rect.centery
                delta_y = dist_y / (float(ms_to_tick) + frame_ms) * frame_ms
                self.rect.centery += delta_y

    def tick_update(self):
        self.rect.center = self.target_x_px, self.target_y_px
        self.x, self.y = self.target_x, self.target_y

        self.ai.progress()
        if MOVE_D in self.ai.states:
            self.target_y = self.y + 1
            self.target_y_px = self.target_y * config.TILE_SIZE
        if MOVE_U in self.ai.states:
            self.target_y = self.y - 1
            self.target_y_px = self.target_y * config.TILE_SIZE
        if MOVE_R in self.ai.states:
            self.target_x = self.x + 1
            self.target_x_px = self.target_x * config.TILE_SIZE
        if MOVE_L in self.ai.states:
            self.target_x = self.x - 1
            self.target_x_px = self.target_x * config.TILE_SIZE


class Worker(BaseMan):
    image_path = 'units/worker1.png'

    def build_field(self):
        return Field(self.x, self.y)

    def tick_update(self):
        super(Worker, self).tick_update()
        if BUILD_FIELD in self.ai.states:
            self.build_field()
