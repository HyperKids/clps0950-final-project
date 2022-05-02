from global_vars import *
from Player import *
from Pipe import *
from Score import *

class Game():
  def __init__(self):
    self.score = Score()
    self.pipes = []
    # Player tutorial used:
    # https://opensource.com/article/17/12/game-python-add-a-player
    self.player = Player()
    self.player.rect.x = (width / 2 - self.player.rect.width / 2) * 3 / 5
    self.player.rect.y = height / 2 - self.player.rect.height / 2
    self.player_list = pygame.sprite.Group()
    self.player_list.add(self.player)
    self.speed = game_speed
    self.base = pygame.image.load(os.path.join('images','base.png')).convert()
    self.base = pygame.transform.scale(self.base, (504, 168))
    self.distance = 0
    self.started = False
    self.start()
  def update(self, dt):
    for pipe in self.pipes:
      pipe.update(dt)
    self.distance += dt
    self.player.update(dt)
  def start(self):
    # only run function once
    if ~self.started:
      self.distance = 0
      self.pipes.append(Pipe(width * 2))
      self.pipes.append(Pipe(width * 2.75))
