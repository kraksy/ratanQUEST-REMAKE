import pygame as py
from pygame.locals import *

py.init()

clock = py.time.Clock()
fps = 60

s_width = 800
s_height = 800

screen = py.display.set_mode((s_width, s_height))
py.display.set_caption('ratan quest')

ground_scroll = 0
scroll_speed = 4

bg = py.image.load('back.jpg')

run = True
while run:

    clock.tick(fps)

    #draw background
    screen.blit(bg, (0,0))

    #draw and scroll the ground
    screen.blit(bg, (ground_scroll, 768))
    ground_scroll -= scroll_speed
    
    if abs(ground_scroll) > 35:
        ground_scroll = 0


    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    py.display.update()

py.quit()