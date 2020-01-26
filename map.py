import pygame

class Map:
    def __init__(self, map_file, positions, color_zero, color_one):
        self.bitmap = list()
        self.positions = positions
        self.color_zero = color_zero
        self.color_one = color_one
        self.load_map_file(map_file)

    def load_map_file(self, map_file):
        with open(map_file, 'r') as f:
            for line in f.readlines():
                self.bitmap.append(line)

    def draw_part(self, window, start, size):
        for i in range(start[0], start[0] + size[0]):
            for j in range(start[1], start[1] + size[1]):
                window.set_at((i, j), self.color_one if self.bitmap[j][i] else self.color_zero) # Поменять цвета местами если баги
