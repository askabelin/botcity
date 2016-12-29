import pygame
import pygame.locals

from map import Level


if __name__ == "__main__":
    screen = pygame.display.set_mode((64 * 14, 64 * 10))
    level = Level('level.map')
    clock = pygame.time.Clock()

    background = level.render()
    screen.blit(background, (0, 0))

    game_over = False
    while not game_over:

        # XXX draw all the objects here

        pygame.display.flip()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                game_over = True
            elif event.type == pygame.locals.KEYDOWN:
                pressed_key = event.key