import pygame
import os
# global variables
global_scale = 1.5 # TODO: make program scalable based on this variable
width, height = 288 * global_scale, 512 * global_scale
max_falling_speed = 12
game_speed = 12
pipe_mvmt = 9 #the actual pipe speed is dt divided by this number
# Set up the window.
screen = pygame.display.set_mode((width, height))
bg = pygame.image.load(os.path.join('images', 'background-day.png')).convert()
bg = pygame.transform.scale(bg, (width, height))

homescreen = pygame.image.load(os.path.join('images', 'homescreen2.png')).convert()
homescreen.set_colorkey((0, 0, 255))
homescreen = pygame.transform.scale(homescreen, (width, height))

endscreen = pygame.image.load(os.path.join('images', 'endscreen.png')).convert()
endscreen.set_colorkey((0, 0, 255))
endscreen = pygame.transform.scale(endscreen, (width, height))
