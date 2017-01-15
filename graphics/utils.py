import pygame


def get_image_grid(image_path, tile_size, transparent=True):
    grid = []
    image = pygame.image.load(image_path)
    image = image.convert_alpha() if transparent else image.convert()
    image_width_px, image_height_px = image.get_size()
    for tile_x in range(0, int(image_width_px / tile_size)):
        line = []
        grid.append(line)
        for tile_y in range(0, int(image_height_px / tile_size)):
            rect = (tile_x * tile_size, tile_y * tile_size, tile_size, tile_size)
            line.append(image.subsurface(rect))
    return grid
