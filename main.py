import pygame as py
from sett import *
from map import *
import random

class gaem:

    screen = py.display.set_mode((WIDTH, HEIGHT))


    def create_texture(color):
        image = py.Surface((TILE_SIZE,TILE_SIZE))
        image.fill(color)
        

    textures = {
    0x0 : create_texture(GREEN),
    0x1 : create_texture(BROWN)
    }


    def draw_map(screen, map_data):
        MAP_HEIGHT = len(map_data) 
        MAP_WIDTH = len(map_data[0])

    def event():
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    py.quit()

    while running:
        event()
        draw_map()

    py.display.update()