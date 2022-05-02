import pygame
import os
# global variables
global_scale = 1.5 # TODO: make program scalable based on this variable
width, height = 288 * global_scale, 512 * global_scale
max_falling_speed = 12
game_speed = 12
# Set up the window.
screen = pygame.display.set_mode((width, height))
bg = pygame.image.load(os.path.join('images', 'background-day.png')).convert()
bg = pygame.transform.scale(bg, (width, height))

#top_pipe = pygame.image.load(os.path.join('images', 'pipe-green.png')).convert()
#top_pipe = pygame.transform.scale(top_pipe, (52, 280))
