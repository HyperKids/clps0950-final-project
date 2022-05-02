import os
import random

from global_vars import *

# constants
pipe_width = 40
gap_size = 120
pipe_speed = 20

game_images = {}
pipe = 'images/pipe-green.png'
base = 'images/base.png'
game_images['base'] = pygame.image.load(base).convert_alpha()
game_images['pipe'] = (pygame.transform.rotate(pygame.image.load(pipe).convert_alpha(), 180),
                             pygame.image.load(pipe).convert_alpha())

def createPipe():
  # offset = height/5
  pipeHeight = 320
  #generating random height of pipes
  y2 = gap_size + random.randrange(0, 84)
  pipeX = pipe_width
  y1 = pipeHeight - y2 + gap_size
  pipe = [
    {'x': pipeX, 'y': -y1}, #upper pipe
    {'x': pipeX, 'y': y2} #lower pipe
  ]
  return pipe


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
