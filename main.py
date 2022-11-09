import pygame as py
import random
 
from map import *
from sett import *
from player import *

py.display.set_caption('ratan quest')

screen = py.display.set_mode((WIDTH, HEIGHT))

def event():
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
       s if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                py.quit()

while running:
    event()


py.display.update()