import os
import random

from global_vars import *

# constants
pipe_width = 40
gap_size = 120
pipe_speed = 20

class Pipe():
  def __init__(self):
    self.x = width
    self.y = random.randint(0, height - gap_size)
    self.width = pipe_width
    self.height = gap_size
    self.speed = pipe_speed
    self.image = pygame.image.load(os.path.join('images', 'pipe.png')).convert_alpha()
    self.image = pygame.transform.scale(self.image, (self.width, self.height))
    self.rect = self.image.get_rect()
    self.rect.x = self.x
    self.rect.y = self.y
  def update(self, dt):
    self.x -= self.speed * dt / 1000
    self.rect.x = self.x
    self.rect.y = self.y
  def draw(self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))
  def offscreen(self):
    return self.x < -self.width
  def collided(self, player):
    return self.rect.colliderect(player.rect)