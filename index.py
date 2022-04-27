# PyGame template from https://gist.github.com/MatthewJA/7544830

import sys

import pygame
from pygame.locals import *

from Player import *

from global_vars import *

## Initialization

# Set up the window.
screen = pygame.display.set_mode((width, height))

# Player tutorial used:
# https://opensource.com/article/17/12/game-python-add-a-player
player = Player()
player.rect.x = (width / 2 - player.rect.width / 2) * 3 / 5
player.rect.y = height / 2 - player.rect.height / 2
player_list = pygame.sprite.Group()
player_list.add(player)
 
def update(dt):
  """
  Update game. Called once per frame.
  dt is the amount of time passed since last frame.
  If you want to have constant apparent movement no matter your framerate,
  what you can do is something like
  
  x += v * dt
  
  and this will scale your velocity based on time. Extend as necessary."""
  
  # Go through events that are passed to the script by the window.
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
      if event.key == pygame.K_UP:
        player.flap()
        pass
    
  # Update player.
  player.update(dt)
 
def draw(screen):
  """
  Draw things to the window. Called once per frame.
  """
  screen.fill((135, 206, 235)) # Fill the screen with blue.
  player_list.draw(screen)
  
  # Redraw screen here.
  
  # Flip the display so that the things we drew actually show up.
  pygame.display.flip()
 
def runPyGame():
  pygame.init()
  
  # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
  fps = 60.0
  fpsClock = pygame.time.Clock()
  
  # Main game loop.
  dt = 1/fps # dt is the time since last frame.
  while True: # Loop forever!
    update(dt) # You can update/draw here, I've just moved the code for neatness.
    draw(screen)
    
    dt = fpsClock.tick(fps)

runPyGame()