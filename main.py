import pygame as py
import sys as sus
from sett import *

class gaem:

    screen = py.display.set_mode((WIDTH, HEIGHT))

    def draw_grid():
        for x in range(0, WIDTH, TILESIZE):
            py.draw.line(py.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            py.draw.line(py.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def event():
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    py.quit()

    while running:
        event()

    py.display.update()