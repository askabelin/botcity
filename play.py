import pygame.display

import config
from graphics.utils import get_image_grid
from graphics.sprites import Villager


pygame.init()
screen = pygame.display.set_mode((config.SCREEN_RES_X, config.SCREEN_RES_Y))
background = pygame.Surface(screen.get_size())

floor_grid = get_image_grid('images/tilesets/floor.png', config.TILE_SIZE, transparent=False)
grass_tile = floor_grid[8][10]

for x in range(config.SCREEN_RES_X / config.TILE_SIZE):
    for y in range(config.SCREEN_RES_Y / config.TILE_SIZE):
        background.blit(grass_tile, (x * config.TILE_SIZE, y * config.TILE_SIZE))

screen.blit(background, (0, 0))

villagers = pygame.sprite.Group()
villager1 = Villager(1, 1, (villagers,))
villager2 = Villager(3, 1, (villagers,))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_w:
                villager1.move_up()
            if event.key == pygame.K_a:
                villager1.move_left()
            if event.key == pygame.K_s:
                villager1.move_down()
            if event.key == pygame.K_d:
                villager1.move_right()

    villagers.clear(screen, background)
    villagers.update()
    villagers.draw(screen)
    pygame.display.flip()
