import pygame as py 
import math as ma
from sett import * 

class menu: 

    py.display.set_caption('ratan quest')
    screen = py.display.set_mode((WIDTH, HEIGHT))

    def load():

        bg = py.image.load("back.jpg").convert()
        pg = py.image.load("title.png").convert_alpha()
        po = py.image.load("op.png").convert_alpha()

        rect = pg.get_rect()
        rect.center = (400,300)

        rect2 = po.get_rect()
        rect2.center = (0,300)

    def event():

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    py.quit()

    def loop():
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

        
    while running:
        load()
        event()
        logo()
        loop()