import os

import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.images = []

    img = pygame.image.load(os.path.join('images', 'flappy-bird.png')).convert()

    img= pygame.transform.scale(img, (50, 50))

    self.images.append(img)
    self.image = self.images[0]
    self.rect = self.image.get_rect()

    # velocity y
    self.vy = 0
    # acceleration y
    self.ay = 0
    # gravity
    self.g = 9.8
  def update(self):
    # update velocity
    self.vy += self.ay
    # update position
    self.y += self.vy
    # update acceleration
    self.ay = self.g