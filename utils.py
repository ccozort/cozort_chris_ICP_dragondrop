import pygame as pg
from settings import *
from math import floor
from collections import deque

class Map:
    def __init__(self, filename):
        self.data = []

        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())
        # for later use
        # self.tilewidth = len(self.data[0])
        # self.tileheight = len(self.data)
        # self.width = self.tilewidth * TILESIZE
        # self.height = self.tileheight * TILESIZE
        print('map instantiated...')

class Spritesheet: 
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0,0), (x,y, width, height))
        # when applying pygame transformation translation rotation and scale we need to pass the newly transformed object into a a new variable
        new_image = pg.transform.scale(image, (width, height))
        image = new_image
        return image


class Cooldown():
    def __init__(self):
        self.current_time = 0
        self.event_time = 0
        self.delta = 0
    def ticking(self):
        self.current_time = floor((pg.time.get_ticks())/1000)
        self.delta = self.current_time - self.event_time
        # print(self.delta)
    def timer(self):
        self.current_time = floor((pg.time.get_ticks())/1000)


def get_grid_pos(pixel_pos):
    """Converts (x, y) pixel coordinates to (col, row) grid indices."""
    return int(pixel_pos[0] // TILESIZE), int(pixel_pos[1] // TILESIZE)


def get_pixel_center(grid_pos):
    """Converts (col, row) grid indices to the center (x, y) of that tile."""
    col, row = grid_pos
    return pg.math.Vector2(
        col * TILESIZE + TILESIZE // 2,
        row * TILESIZE + TILESIZE // 2
    )


def bfs_path(grid, start, goal):
    """Returns the shortest path from start to goal as a list of (col, row) tuples."""
    if start == goal:
        return []

    queue = deque([start])
    came_from = {
        start: None
        }
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Up, Down, Left, Right

    while queue:
        current = queue.popleft()

        if current == goal:
            break

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)

            # Check grid bounds, walkability, and if already visited
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                if grid[ny][nx] == 0 and neighbor not in came_from:
                    queue.append(neighbor)
                    came_from[neighbor] = current

    # Reconstruct path if goal was reached
    if goal not in came_from:
        return []

    path = []
    curr = goal
    while curr != start:
        path.append(curr)
        curr = came_from[curr]
    path.reverse()
    return path