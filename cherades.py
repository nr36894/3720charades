import pygame
import random
import math
import time
from datamuse import datamuse
from pygame.constants import K_1

api = datamuse.Datamuse()
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
counter, text = 10, '10'.rjust(3)
font = pygame.font.SysFont('Consolas', 30)

pygame.time.set_timer(pygame.USEREVENT, 1000)
pygame.display.set_caption('Let\'s Play Charades')

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

# important variables
running = True
points = [0,0]

# Background color of screen
def screenColor():
    screen.fill(black)


def getWord():
    print("get word")
    # get the word


def generateButtons():
    print("genere buttons")
    # add remove points

    # show/hide word

    # skip word

def showScore(choice=1):
    # Team 1
    text1 = ""
    text2 = ""
    sFont = pygame.font.SysFont('arial', 35)
    
    # Score shown during game play with each team's points
    # Scores will be shown in upper left hand corner
    if choice == 1:
        text1 = "Team 1 Score: " + str(points[0])
        text2 = "Team 2 Score: " + str(points[1])
        t1surf = sFont.render(text1, True, white)
        t1rect = t1surf.get_rect()
        t1rect.topleft = (140, 10)
        screen.blit(t1surf, t1rect)
        t2surf = sFont.render(text2, True, white)
        t2rect = t2surf.get_rect()
        t2rect.topleft = (140, 50)
        screen.blit(t2surf, t2rect)
    # At end, winner/tie is shown with the number of points
    # Statement shown in upper middle of screen
    else:
        if points[0] > points[1]:
            text1 = "Team 1 Wins w/ " + str(points[0]) + " Points"
        elif points[1] > points[0]:
            text1 = "Team 2 Wins w/ " + str(points[1]) + " Points"
        else:
            text1 = "Tie w/ " + str(points[0]) + " Points"
        t1surf = sFont.render(text1, True, white)
        t1rect = t1surf.get_rect()
        t1rect.midtop = (400, 120)
        screen.blit(t1surf, t1rect)

while running:
    screenColor()

    # Display player names
    
    # Get and display player scores

    # Display current actor

    # Get and display current word

    # Display buttons

    # Display

    # Demo to show how score is shown 
    if points[0] < 10 and points[1] < 10:
        showScore() # To show the score
    else:
        showScore(0) # To show winner/tie

    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
            print("test")
            counter -= 1
            text = str(counter).rjust(3)if counter > 0 else 'Game Over!'
        elif event.type == pygame.QUIT:
            running = False
        # Temporary elif statement to show how points can be added to a team
        elif event.type == pygame.KEYDOWN:
            # Pressing 1 adds to team 1
            if event.key == pygame.K_1:
                points[0] += 1
            # Pressing 2 adds to team 2
            elif event.key == pygame.K_2:
                points[1] += 1
    
    screen.blit(font.render(text, True, white), (320, 480))
    pygame.display.flip()
    clock.tick(60)