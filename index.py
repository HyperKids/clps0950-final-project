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
      if event.key == pygame.K_UP:
        game.player.flap()
        pass

  # Update level
  game.update(dt)
 
def draw(screen):
  """
  Draw things to the window. Called once per frame.
  """
  screen.blit(bg, (0, 0)) # Fill the screen with background.
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
  for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
    screen.blit(game_images['pipe'][0], (upperPipe['x'], upperPipe['y']))
    screen.blit(game_images['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

  game.player_list.draw(screen)

  # render ground last so it covers other items visually
  screen.blit(game.base, (-((game.distance / 10) % 36), height-84))

  # Redraw screen here.
  
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
