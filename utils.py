import pygame as pg
from settings import *
from math import floor

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


    