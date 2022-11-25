import pygame as py
import sys
from os import path
from settings import * 

class ratan : 

    def __init__(self):

        py.init()
        self.screen = py.display.set_mode((width, height))
        py.display.set_caption(title)
        self.clock = py.time.Clock()
        py.key.set_repeat(500,100)
        

    def load(self):

        ratan_folder = path.dirname(__file__)
        self.mapdata = []
        with open(path.join(ratan_folder, 'map.txt')) as f:
            pass

    def block(self):
        py.draw.rect(surface, color, rect)

    def background(self):
        self.screen.fill(red)
        
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