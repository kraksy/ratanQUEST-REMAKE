import pygame as py
import sys as sus
from sett import *


class gaem:

    screen = py.display.set_mode(WIDTH, HEIGHT)

    def draw_grid():
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def event():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    py.display.update()

    def quit():
        py.quit()
        sus.exit()