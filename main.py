import pygame as py
from map import *
from sett import *
import random

class gaem:
    py.display.set_caption('ratan quest') 
    screen = py.display.set_mode((WIDTH, HEIGHT))


    def create_texture(color):
        image = py.Surface((TILE_SIZE,TILE_SIZE))
        image.fill(color)
        

    textures = {
    0 : create_texture(GREEN),
    1 : create_texture(BROWN)
    }

    def event():
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    py.quit()

    while running:
        event()

        if tile 


    py.display.update()