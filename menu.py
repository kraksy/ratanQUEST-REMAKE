import pygame as py
import math 

running = True

while running:
    py.init()


    def event():
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    py.quit()

    FrameHeight = 800
    FrameWidth = 800

    clock = py.time.Clock()

    py.display.set_caption("ratan quest")
    screen = py.display.set_mode((FrameWidth, FrameHeight))


    bg = py.image.load("back.jpg").convert()
    pg = py.image.load("title.png").convert_alpha()
    po = py.image.load("op.png").convert_alpha()

    scroll = 0
    tiles = math.ceil(FrameWidth  /bg.get_width()) + 1   


    def start():
        print()

    def quit():
        print()

    def sett():
        print()

    while 1:
        clock.tick(33)

        rect = pg.get_rect()
        rect.center = (400,300)

        rect2 = po.get_rect()
        rect2.center = (0,300)
    
        i = 0
        while(i < tiles):
            screen.blit(bg, (bg.get_width()*i
                        + scroll, 0))
            i += 1

            screen.blit(po, (rect2.center))
            screen.blit(pg, (rect.center))

        #speeeeeed
        scroll -= 2
  

        py.display.update()

py.quit()