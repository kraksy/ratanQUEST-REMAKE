from pytmx.util_pygame import load_pygame
import pygame as py
from pathlib import Path
import pyscroll

# some variables for something

CURRENT_DIR = Path(__file__).parent
RESOURCES_DIR = CURRENT_DIR / "data"
HERO_MOVE_SPEED = 200

def init_screen(width: int, height: int) -> py.SurFace:
    screen = py.display.set_mode((width, height), py.RESIZABLE)
    return screen

# this shit said that it will be easy to load image

def load_image(filename: str) -> py.Surface:
    return py.image.load(str(RESOURCES_DIR / filename))

class character:
    #i need some help, but im alone\

    print()

class game:

    #please god help me
    print()
