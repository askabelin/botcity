import pygame
import ConfigParser


def load_tile_table(filename, size):
    image = pygame.image.load(filename).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, image_width / size):
        line = []
        tile_table.append(line)
        for tile_y in range(0, image_height / size):
            rect = (tile_x * size, tile_y * size, size, size)
            line.append(image.subsurface(rect))
    return tile_table


MAP_TILE_SIZE = 64
TILE_SET = 'tile_set.png'


class Level(object):
    def __init__(self, filename="level.map"):
        self.map = []
        self.key = {}
        self.tile_table = load_tile_table('tile_set.png', MAP_TILE_SIZE)

        parser = ConfigParser.ConfigParser()
        parser.read(filename)
        self.map = parser.get("level", "map").split("\n")
        for section in parser.sections():
            if len(section) == 1:
                desc = dict(parser.items(section))
                self.key[section] = desc
        self.width = len(self.map[0])
        self.height = len(self.map)

    def get_tile(self, x, y):
        try:
            char = self.map[y][x]
        except IndexError:
            return {}
        try:
            return self.key[char]
        except KeyError:
            return {}

    def get_tile_property(self, x, y, name):
        return self.get_tile(x, y).get(name)

    def same_type(self, x1, y1, x2, y2):
        return self.map[y1][x1] == self.map[y2][x2]

    def render(self):
        image = pygame.Surface((self.width * MAP_TILE_SIZE, self.height * MAP_TILE_SIZE))
        for x, line in enumerate(self.map):
            for y, c in enumerate(line):
                tile = self.get_tile(x, y)
                tile_image_x, tile_image_y = map(int, tile['image'].split(', '))
                if tile.get('has_border'):
                    left = self.same_type(x, y, x - 1, y)
                    right = self.same_type(x, y, x + 1, y)
                    up = self.same_type(x, y, x, y + 1)
                    down = self.same_type(x, y, x, y - 1)
                    if up and down and left and right:
                        if not self.same_type(x, y, x + 1, y - 1):
                            tile_image_x += 2
                        elif not self.same_type(x, y, x - 1, y - 1):
                            tile_image_x += 3
                        elif not self.same_type(x, y, x + 1, y + 1):
                            tile_image_x += 2
                            tile_image_y -= 1
                        elif not self.same_type(x, y, x - 1, y + 1):
                            tile_image_x += 3
                            tile_image_y -= 1
                    else:
                        if not left:
                            tile_image_x -= 1
                        if not right:
                            tile_image_x += 1
                        if not up:
                            tile_image_y += 1
                        if not down:
                            tile_image_y -= 1
                tile_image = self.tile_table[tile_image_x][tile_image_y]
                image.blit(tile_image, (x * MAP_TILE_SIZE, y * MAP_TILE_SIZE))
        return image
