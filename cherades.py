import pygame
import random
import math
import time
from datamuse import datamuse

api = datamuse.Datamuse()
pygame.init()

screen = pygame.display.set_mode((800, 600))

def addName(name):
    print("add name")
    # add the name


def getWord():
    print("get word")
    # get the word


def generateButtons():
    print("genere buttons")
    # add remove points

    # show/hide word

    # skip word


running = True
while running:
    screen.fill((0, 0, 0))

    # Display player names
    
    # Get and display player scores

    # Display current actor

    # Get and display current word

    # Display buttons

    # Display 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False