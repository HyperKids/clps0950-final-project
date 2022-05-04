# PyGame template from https://gist.github.com/MatthewJA/7544830

import sys

import pygame
from pygame.locals import *

from Game import *

from global_vars import *
from Pipe import *

## Initialization
# Screen pulled from global_vars.py

game = Game()

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
      if event.key == pygame.K_SPACE:
        if game.start_screen:
          game.start_screen = False
        elif game.started == False:
          game.start()
          game.player.flap()
        else:
          game.player.flap()
        pass
    if event.type == pygame.MOUSEBUTTONDOWN:
      if game.start_screen:
        game.start_screen = False
      elif game.started == False:
        game.start()
        game.player.flap()
      else:
        game.player.flap()

  # Update level
  game.update(dt)
 
def draw(screen):
  """
  Draw things to the window. Called once per frame.
  """
  screen.blit(bg, (0, 0)) # Fill the screen with background.

  screen.blit(game.base, (-((game.distance / 10) % 36), height-84))

  for pipe in game.pipes:
    pipe.pipe_list.draw(screen)
  game.player_list.draw(screen)
  
  if game.started:
    game.score.draw()

  # render ground last so it covers other items visually
  screen.blit(game.base, (-((game.distance / 10) % 36), height-84))

  # Draw menu if there should be a menu.
  if game.start_screen:
    screen.blit(bg, (0, 0)) # Fill the screen with menu.
  
  # Flip the display so that the things we drew actually show up.
  pygame.display.flip()



def runPyGame():
  pygame.init()

  pygame.display.set_caption('Flappy Bird')

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
