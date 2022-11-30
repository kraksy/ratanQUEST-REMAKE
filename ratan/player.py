import pygame as py
from settings import *

class Player(py.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        py.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = py.Surface((tile,tile))
        self.image.fill(gray)
        self.rect = self.image.get_rect()