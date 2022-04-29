from global_vars import *
from Player import *

class Game():
  def __init__(self):
    self.score = 0
    self.pipes = []
    # Player tutorial used:
    # https://opensource.com/article/17/12/game-python-add-a-player
    self.player = Player()
    self.player.rect.x = (width / 2 - self.player.rect.width / 2) * 3 / 5
    self.player.rect.y = height / 2 - self.player.rect.height / 2
    self.player_list = pygame.sprite.Group()
    self.player_list.add(self.player)
    self.speed = 12
    self.base = pygame.image.load(os.path.join('images','base.png')).convert()
    self.base = pygame.transform.scale(self.base, (504, 168))
    self.distance = 0
  def update(self, dt):
    for pipe in self.pipes:
      pipe.update(dt)
    for pipe in self.pipes:
      if pipe.offscreen():
        self.pipes.remove(pipe)
    for pipe in self.pipes:
      if pipe.collided(self.player):
        self.score = 0
        self.pipes = []
        self.player.rect.x = (width / 2 - self.player.rect.width / 2) * 3 / 5
        self.player.rect.y = height / 2 - self.player.rect.height / 2
    self.distance += dt
    self.player.update(dt)
