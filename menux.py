import pygame as py 
import math as ma
from sett import *

class menu: 

    py.display.set_caption('ratan quest')
    screen = py.display.set_mode((WIDTH, HEIGHT))

    def event():

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    py.quit()

    def loop(bg , pg , po):
        while running:
            clock.tick(60)

            i = 0 
            while(i < tiles):
                screen.blit(bg, (bg.get_width()*i
                            + scroll , 0))
                i =+ 1

            scroll -= 2

            py.display.update()

    def logo():
        while running:
            screen.blit(po, (rect2.center))
            screen.blit(pg, (rect.center))

    def switch():
        print()

    while running:
        load()
        event()
        logo()
        loop()

