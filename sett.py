import pygame as py
import math

try :

    WIDTH = int(1024)
    HEIGHT = int(768)

    FrameHeight = 1024
    FrameWidth = 768

    def load():

        bg = py.image.load("src/back.jpg").convert()
        pg = py.image.load("src/title.png").convert_alpha()
        po = py.image.load("src/op.png").convert_alpha()

        rect = pg.get_rect()
        rect.center = (400,300)

        rect2 = po.get_rect()
        rect2.center = (0,300)

    TILE_SIZE = 32

    LIGHTGREY = (100, 100, 100)

    running = True

    clock = py.time.Clock()

    tiles = math.ceil(FrameWidth /bg.get_width()) + 1
d
    YELLOW  = (255, 255, 0)
    RED     = (255, 0, 0)
    BLUE    = (0 , 0, 255)
    GREEN   = (0, 255, 0)

    load()

except Exception as i:
    print(i)