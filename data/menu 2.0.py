import pygame as py
import math

py.init()

clock = py.time.Clock()
FPS = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption("ratan")

bg = py.image.load("back.jpg").convert()
pg = py.image.load("title.png").convert_alpha()
po = py.image.load("op.png").convert_alpha()

bg_width = bg.get_width()
bg_rect = bg.get_rect()

rect = pg.get_rect()
rect.center = (400,300)

rect2 = po.get_rect()
rect2.center = (0,300)

scroll = 0
tiles = math.ceil(SCREEN_WIDTH  / bg_width) + 1


run = True
while run:

  clock.tick(FPS)

  for i in range(0, tiles):
    screen.blit(bg, (i * bg_width + scroll, 0))
    screen.blit(po, (i * 800 + scroll, 300))
    screen.blit(pg, (rect.center))

    bg_rect.x = i * bg_width + scroll
    py.draw.rect(screen, (255, 0, 0), bg_rect, 1)

  scroll -= 6

  if abs(scroll) > bg_width:
    scroll = 0

  for event in py.event.get():
    if event.type == py.QUIT:
      run = False

  py.display.update()

py.quit()