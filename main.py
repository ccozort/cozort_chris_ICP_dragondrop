# This file was created by: Chris Cozort
# Content inspired by: Chris Bradfield
# I do solemnly swear to create concise and informative comments

'''
The game engine consists of three (four) basic components:
Input - keys, buttons, voice, mouse, touch, breath, movement, control stick
Process - input processed (direction of control, magnitude)
Output - Draw new frames pixels, sound, haptics (senses)
(Store)
change test


GOALS: Collect Dragon Eggs 
RULES: Have to do it in a certain amount of time
FEEDBACK: 
FREEDOM: 
'''

import pygame as pg
from os import path
from settings import *
from sprites import *
from utils import *


# the game class a blueprint for the whole game...
class Game:
    # 
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        print('game class initialized')
        self.clock = pg.time.Clock()
        self.running = True
        self.playing = True

    def load_data(self, map):
        self.game_dir = path.dirname(__file__)
        self.img_dir = path.join(self.game_dir, 'images')
        self.snd_dir = path.join(self.game_dir, 'sounds')
        self.map = Map(path.join(self.game_dir, map))

    def new(self):
        self.load_data('level1.txt')
        self.all_sprites = pg.sprite.Group()
        self.all_walls = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        # instantiate player here
        
        self.wall = Wall(self,5,0)
        print(self.map.data)
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'M':
                    Mob(self, col, row)
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == 'P':
                    self.player = Player(self, col, row)

    def run(self):
        while self.running:
            # sets the delta time property and runs the tick function at FPS/1000
            self.dt = self.clock.tick(FPS) / 1000
            self.events() # this gets player input
            self.update() # this updates the game
            self.draw() # this draws sprites
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    # this block of code handles processing of changes based on input
    def update(self):
        self.all_sprites.update()
    # draw text on screen anywhere 
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        # instantiate the Font class
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        self.draw_text("Frames per second: " + str(floor(1/self.dt) ), 24, WHITE, WIDTH/2, HEIGHT/4)
        pg.display.flip()

if __name__ == "__main__":
    g = Game()

while g.running:
    g.new()
    g.run()

pg.quit()
