import pygame as py
import math 
import random 
import sys

from settings import *

py.display.set_caption('ratan quest')
screen = py.display.set_mode((width, height))

pg = py.image.load("src/title.png").convert_alpha()
po = py.image.load("src/op.png").convert_alpha()


rect = pg.get_rect()
rect.center = (400,300)

rect2 = po.get_rect()
rect2.center = (0,300)

bg = py.image.load("src/back.jpg").convert()
bg = py.transform.scale(bg, (width, height))


def event():
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                py.quit()

def loop():

    i = 0

    screen.fill((0,0,0))
    screen.blit(bg,(i,0))
    screen.blit(bg,(width+i,0))

    if i == -width:
        screen.blit(bg, (width+i,0))
        i=0
    i-=1

    py.display.update()
    

def logo():
    screen.blit(po, (rect2.center))
    screen.blit(pg, (rect.center))

    py.display.update()

while running:
    event()
    loop()
