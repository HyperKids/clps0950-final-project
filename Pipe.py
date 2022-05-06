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


class TopPipe(pygame.sprite.Sprite):
  def __init__(self, x, height):
    pygame.sprite.Sprite.__init__(self)
    #self.y = random.randint(0, height - gap_size)
    #self.width = pipe_width
    self.image = pygame.image.load(os.path.join('images', 'pipe-green.png')).convert_alpha()
    self.image = pygame.transform.flip(self.image, False, True)
    self.image = pygame.transform.scale(self.image, (78, 420))
    self.gap = 170
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = height - self.image.get_height()
  def update(self, dt):
    self.rect.x -= dt / pipe_mvmt
    if self.rect.x < 0:
      self.rect.x -= dt/pipe_mvmt
  # check if pipe is offscreen
  def offscreen(self):
    return self.rect.x < -self.image.get_width()
  def moveto(self, x, height):
    self.rect.x = x
    self.rect.y = height - self.image.get_height()

class BotPipe(pygame.sprite.Sprite):
  def __init__(self, x, height):
    pygame.sprite.Sprite.__init__(self)
    #self.y = random.randint(0, height - gap_size)
    #self.width = pipe_width
    self.image = pygame.image.load(os.path.join('images', 'pipe-green.png')).convert_alpha()
    self.image = pygame.transform.scale(self.image, (78, 420))
    self.gap = 170
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = height + self.gap
  def update(self, dt):
    self.rect.x -= dt / pipe_mvmt
    if self.rect.x < 0:
      self.rect.x -= dt/pipe_mvmt
  # check if pipe is off screen
  def offscreen(self):
    return self.rect.x < -self.image.get_width()
  def moveto(self, x, height):
    self.rect.x = x
    self.rect.y = height + self.gap


class PipeSet(pygame.sprite.Sprite):
  def __init__(self, x):
    pygame.sprite.Sprite.__init__(self)
    self.height = self.random_height()
    self.top_pipe = TopPipe(x, self.height)
    self.bottom_pipe = BotPipe(x, self.height)
    self.pipe_list = pygame.sprite.Group(self.top_pipe, self.bottom_pipe)
  def update(self, dt):
    self.top_pipe.update(dt)
    self.bottom_pipe.update(dt)
    if self.top_pipe.offscreen() or self.bottom_pipe.offscreen():
      self.height = self.random_height()
      self.top_pipe.moveto(width * 1.5 - (self.top_pipe.image.get_width()), self.height)
      self.bottom_pipe.moveto(width * 1.5 - (self.bottom_pipe.image.get_width()), self.height)
  def random_height(self):
    return random.randrange(90, 400)
