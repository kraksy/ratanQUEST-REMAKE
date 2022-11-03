import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, sprites_group, pos, dim, col):
        self.groups = sprites_group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.Surface(dim)
        self.image.fill(col)

        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        self.get_event()

    def get_event(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(0, -5)
        if keys[pygame.K_s]:
            self.move(0, +5)
        if keys[pygame.K_a]:
            self.move(-5, 0)
        if keys[pygame.K_d]:
            self.move(+5, 0)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy