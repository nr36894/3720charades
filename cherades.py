import pygame
import random
import math
from datamuse import datamuse

api = datamuse.Datamuse()
pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False