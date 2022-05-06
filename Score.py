import pygame
from global_vars import *

class Score():
  def __init__(self):
    self.score = 0
  def add(self):
    self.score += 1
  def get(self):
    return self.score
  def reset(self):
    self.score = 0
  def draw(self):
    digits = [int(x) for x in str(self.score)]
    for i in range(len(digits)):
      digit = digits[i]
      img = pygame.image.load(os.path.join('images', str(digit)+'.png')).convert_alpha()
      img = pygame.transform.scale(img, (24 * global_scale, 36 * global_scale))
      # draw score in top center of screen
      screen.blit(img, (width / 2 - (len(digits) / 2 - i) * 24 * global_scale, 36 * global_scale))
  def draw_final(self):
    digits = [int(x) for x in str(self.score)]
    for i in range(len(digits)):
      digit = digits[i]
      img = pygame.image.load(os.path.join('images', str(digit)+'.png')).convert_alpha()
      # draw score on right center of screen
      screen.blit(img, (width - 73 - (len(digits) - i) * 24 * global_scale * 2 / 3, height / 2 + 5 - 36 * global_scale * 2 / 3))