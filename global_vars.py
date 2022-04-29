import pygame
import os
# global variables
width, height = 432, 768
# Set up the window.
screen = pygame.display.set_mode((width, height))
bg = pygame.image.load(os.path.join('images', 'background-day.png'))
bg = pygame.transform.scale(bg, (width, height))
