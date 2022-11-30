import pygame as py
import sys
from os import path
from settings import * 
from player import *
from sprites import *

class ratan : 

    def __init__(self):

        py.init()
        self.screen = py.display.set_mode((width, height))
        py.display.set_caption(title)
        self.clock = py.time.Clock()
        py.key.set_repeat(500,100)

    def background(self):

        self.screen.fill(red)

        for x in range(width):
            for y in range(height):
                rect = py.Rect(x*blocksize, y*blocksize, blocksize, blocksize)

                py.draw.rect(self.screen, gray, rect, 1)
    
    def player_movement():

        self.playerpos = [0,0]
        self.player = Player(self)

        if event.type == KEYDOWN:
            if event.key == K_RIGHT and playerpos[0] < width -1:
                playerpos[0] += 1
            if event.key == K_LEFT and playerpos[0] < 0:
                playerpos[0] -= 1
            if event.key == K_DOWN and playerpos[1] < height -1:
                playerpos[1] += 1
            if event.key == K_UP and playerpos[1] < 0:
                playerpos[1] -= 1

            self.screen.blit(player,(playerpos[0]*tile,playerpos[1]*tile))
            
    def run(self):

        self.playing = True

        while self.playing:

            self.background()
            self.events()
            self.dt = self.clock.tick(fps) / 1000
            py.display.update()
    
    def events(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                self.quit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    py.quit()

    def quit(self):
        py.quit()
        sys.exit()

game = ratan()
while True:
    game.run()