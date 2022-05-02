import os
import math

import pygame

from global_vars import *

class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.images = []
    for i in range(1, 4):
      img = pygame.image.load(os.path.join('images', 'yellowbird'+str(i)+'.png')).convert_alpha()
      img = pygame.transform.scale(img, (51, 36))
      img = pygame.transform.rotate(img, 0)
      self.images.append(img)
      self.image = self.images[0]
      self.rect = self.image.get_rect()
      self.image_index = 0
      self.frame_count = 0
      self.alive = True

    # velocity y
    self.vy = 0
    # acceleration y
    self.ay = 0
    # gravity
    self.g = 10 / 15 * 60
    # time since last flap in ms, to calculate angle
    self.time_since_flap = 0 # in ms
  def update(self, dt, game):
    self.frame_count += 1
    self.detectCollide(game)
    # if player is in free fall
    if self.vy >= max_falling_speed:
      # set wings to neutral glide position
      self.image_index = 0
    else:
      self.image_index = math.floor(self.frame_count / 4) % 3
    # update time since last flap in ms
    self.time_since_flap += dt
    # update velocity
    self.vy += self.ay * dt / 1000
    # enforce maximum falling speed
    if self.vy > max_falling_speed:
      self.vy = max_falling_speed
    # update position
    self.rect.y += self.vy
    # update acceleration
    self.ay = self.g
    # detect collision with roof and floor, and stop it
    if self.rect.top <= 0:
      self.rect.top = 0
    if self.rect.bottom >= height - 84:
      self.rect.bottom = height - 84
      if self.alive:
        self.die()

    # if not dead
    if self.alive:
      # update bird angle based on time since flap
      if self.time_since_flap < 625:
        # set angle fixed to 20 degrees up
        self.image = pygame.transform.rotate(self.images[self.image_index], 20)
      elif self.time_since_flap < 925:
        # set angle proportional to time since last flap
        self.image = pygame.transform.rotate(self.images[self.image_index], 20 + (self.time_since_flap - 625) / 300 * -110)
      else:
        # set angle fixed to 90 degrees down
        self.image = pygame.transform.rotate(self.images[self.image_index], -90)

  def flap(self):
    if self.alive:
      self.vy = -12 # should this equal max falling speed, but negative?
      self.time_since_flap = 0

  def detectCollide(self, game):
    # detect player collision with pipes
    for pipe in game.pipes:
      if pygame.sprite.collide_rect(self, pipe.top_pipe) or pygame.sprite.collide_rect(self, pipe.bottom_pipe):
        self.die()

  def die(self):
    # only permit death once
    if self.alive:
      self.alive = False
      self.vy = 0
      self.image = pygame.transform.rotate(self.images[self.image_index], -90)