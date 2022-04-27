import os

import pygame

from global_vars import *

class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.images = []

    img = pygame.image.load(os.path.join('images', 'flappy-bird.png')).convert_alpha()

    img = pygame.transform.scale(img, (65, 50))
    img = pygame.transform.rotate(img, 0)

    self.images.append(img)
    self.image = self.images[0]
    self.rect = self.image.get_rect()

    # velocity y
    self.vy = 0
    # acceleration y
    self.ay = 0
    # gravity
    self.g = 10 / 15 * 60
    # time since last flap in ms, to calculate angle
    self.time_since_flap = 0 # in ms
  def update(self, dt):
    # update time since last flap in ms
    self.time_since_flap += dt
    # update velocity
    self.vy += self.ay * dt / 1000
    # enforce maximum falling speed
    if self.vy > 12:
      self.vy = 12
    # update position
    self.rect.y += self.vy
    # update acceleration
    self.ay = self.g
    if self.rect.top <= 0:
        self.rect.top = 0
    if self.rect.bottom >= height:
        self.rect.bottom = height

    # update bird angle based on time since flap
    if self.time_since_flap < 625:
      # set angle fixed to 20 degrees up
      self.image = pygame.transform.rotate(self.images[0], 20)
    elif self.time_since_flap < 925:
      # set angle proportional to time since last flap
      self.image = pygame.transform.rotate(self.images[0], 20 + (self.time_since_flap - 625) / 300 * -110)
    else:
      # set angle fixed to 90 degrees down
      self.image = pygame.transform.rotate(self.images[0], -90)

  def flap(self):
    self.vy = -12
    self.time_since_flap = 0