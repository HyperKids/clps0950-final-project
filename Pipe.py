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
  def __init__(self, x):
    self.x = x
    #self.y = random.randint(0, height - gap_size)
    #self.width = pipe_width
    self.top_pipe = pygame.image.load(os.path.join('images', 'pipe-green.png')).convert_alpha()
    self.top_pipe = pygame.transform.flip(self.top_pipe, False, True)
    self.top_pipe = pygame.transform.scale(self.top_pipe, (78, 420))
    self.bot_pipe = pygame.image.load(os.path.join('images', 'pipe-green.png')).convert_alpha()
    self.bot_pipe = pygame.transform.scale(self.bot_pipe, (78, 420))
    self.height = random.randrange(32, 400)
    self.gap = 120
    self.top = self.height - self.top_pipe.get_height()
    self.bottom = self.height + self.gap
    self.speed = game_speed
    self.rect_top = self.top_pipe.get_rect()
    self.rect_top.x = self.x
    self.rect_top.y = self.top
  def update(self, dt):
    self.x -= dt / 10
    self.rect_top.x = self.x
    self.rect_top.y = self.top
  # def move(self):
  #   self.x -= self.vel
  def draw(self, screen):
    screen.blit(self.top_pipe, (self.x, self.top))
    screen.blit(self.bot_pipe, (self.x, self.bottom))
  def offscreen(self):
    return self.x < -self.width
  def collided(self, player):
    return self.rect.colliderect(player.rect)
  def pipeGame(self):
    first_pipe = createPipe()
    second_pipe = createPipe()
    mytempheight = 100
    down_pipes = [
      {'x': width+300-mytempheight, 'y':first_pipe[1]['y']},
      {'x': width+200-mytempheight+(width/2), 'y':second_pipe[1]['y']}
    ]
    up_pipes = [
      {'x': width+300-mytempheight, 'y':first_pipe[0]['y']},
      {'x': width+200-mytempheight+(width/2), 'y':second_pipe[0]['y']}
    ]
    pipeVelX = -4
    for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
      upperPipe['x'] += pipeVelX
      lowerPipe['x'] += pipeVelX
    if 0 < up_pipes[0]['x'] < 5:
      newpipe = createPipe()
      up_pipes.append(newpipe[0])
      down_pipes.append(newpipe[1])
    if up_pipes[0]['x'] < -game_images['pipe'][0].get_width():
      up_pipes.pop(0)
      down_pipes.pop(0)
