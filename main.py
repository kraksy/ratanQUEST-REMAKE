from pytmx.util_pygame import load_pygame
import pygame as py
import pyscroll

FrameHeight = 800
FrameWidth = 800

py.display.set_caption("ratan quest")
screen = py.display.set_mode((FrameWidth, FrameHeight))


class Sprite(pygame.sprite.Sprite):

    def __init__(self, surface):
        self.image = surface
        self.rect = surface.get_rect()


tmx_data = load_pygame("desert.tmx")

map_layer = pyscroll.BufferedRenderer(
    map_data=pyscroll.TiledMapData(tmx_data),
    screen_size=(400,400),
)

group = pyscroll.PyscrollGroup(map_layer=map_layer)

surface = pygame.image.load("my_surface.png").convert_alpha()
sprite = Sprite(surface)
group.add(sprite)

group.center(sprite.rect.center)

group.draw(screen)