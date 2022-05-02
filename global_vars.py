import pygame
import os
# global variables
width, height = 432, 768
game_speed = 12
# Set up the window.
screen = pygame.display.set_mode((width, height))
bg = pygame.image.load(os.path.join('images', 'background-day.png')).convert()
bg = pygame.transform.scale(bg, (width, height))

#top_pipe = pygame.image.load(os.path.join('images', 'pipe-green.png')).convert()
#top_pipe = pygame.transform.scale(top_pipe, (52, 280))
