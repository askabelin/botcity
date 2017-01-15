import pygame

import config
from graphics.base import all_sprites
from graphics.man import Worker
from logic.man import MOVE_L, MOVE_D, MOVE_U, MOVE_R, BUILD_FIELD

STATE_MAP = {
    pygame.K_w: MOVE_U, pygame.K_a: MOVE_L, pygame.K_s: MOVE_D, pygame.K_d: MOVE_R,
    pygame.K_b: BUILD_FIELD
}

pygame.init()
screen = pygame.display.set_mode((config.SCREEN_RES_X, config.SCREEN_RES_Y))
background = pygame.Surface(screen.get_size())

grass_tile = pygame.image.load('images/terrain/grass1.png').convert()

for x in range(config.SCREEN_RES_X / config.TILE_SIZE):
    for y in range(config.SCREEN_RES_Y / config.TILE_SIZE):
        background.blit(grass_tile, (x * config.TILE_SIZE, y * config.TILE_SIZE))

screen.blit(background, (0, 0))

worker1 = Worker(1, 1)
# worker2 = Worker(3, 1)

running = True
clock = pygame.time.Clock()
next_tick = pygame.time.get_ticks() + config.GAME_SPEED

while running:
    frame_ms = clock.tick(config.FPS)
    ms_to_tick = next_tick - pygame.time.get_ticks()
    pygame.display.set_caption('framerate: {}'.format(clock.get_fps()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            worker1.ai.next_state = worker1.ai.next_state or STATE_MAP.get(event.key)
            if event.key == pygame.K_ESCAPE:
                running = False

    if ms_to_tick <= 0:
        ms_to_tick = 0
        next_tick += config.GAME_SPEED

    all_sprites.clear(screen, background)
    all_sprites.update(frame_ms, ms_to_tick)
    all_sprites.draw(screen)

    pygame.display.flip()
