import pygame
import random
import math
import time
from datamuse import datamuse

api = datamuse.Datamuse()
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Let\'s Play Charades')
font = pygame.font.SysFont('arial', 50)

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

# Background color of screen
def screenColor():
    screen.fill(black)

# See if player wants to play in teams or individuals
def checkTeams():
    Surf = font.render('Play in Teams (T) or Solo (S)?', True, white)
    Rect = Surf.get_rect()
    Rect.center = screen.get_rect().center
    screen.blit(Surf, Rect)
    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # Press "t" for team and "s" for solo
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    return True
                elif event.key == pygame.K_s:
                    return False

# Get the number of players in the game
# Must be greater than 0
def getNumPlayers():
    num = 0
    string_num = ""
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                # Adds it to string if it is numeric
                if event.unicode.isnumeric():
                    string_num += event.unicode
                # Removes number for string if backspace is pressed
                elif event.key == pygame.K_BACKSPACE:
                    string_num = string_num[:-1]
                # Press enter to turn string to number and check if it's greater than 0
                # Will clear and repeat if 0
                elif event.key == pygame.K_RETURN:
                    num = int(string_num)
                    if num > 0:
                        return num
                    string_num = ""
        screenColor()
        Surf = font.render('Enter Number of Players', True, (255, 255, 255))
        Rect = Surf.get_rect()
        Rect.midtop = (400, 100)
        screen.blit(Surf, Rect)
        Surf = font.render(string_num, True, (255, 255, 255))
        Rect = Surf.get_rect()
        Rect.center = screen.get_rect().center
        screen.blit(Surf, Rect)
        pygame.display.flip()

# Have user enter the names of the players
def addName(numP):
    name = ""
    num = 0
    player = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                # Adds letters to names
                if event.unicode.isalpha():
                    name += event.unicode
                # Adds space to name
                elif event.key == pygame.K_SPACE:
                    name += event.unicode
                # Deletes last letter if backspace is pressed
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                # Adds name to list of players
                # Repeats until number of players is reached
                elif event.key == pygame.K_RETURN:
                    if len(name) > 0:
                        player.append(name)
                        num += 1
                        if len(player) == numP:
                            return player
                    name = ""
        screenColor()
        Surf = font.render('Number of players entered: ' + str(num), True, (255, 255, 255))
        Rect = Surf.get_rect()
        Rect.midtop = (400, 100)
        screen.blit(Surf, Rect)
        Surf = font.render(name, True, (255, 255, 255))
        Rect = Surf.get_rect()
        Rect.center = screen.get_rect().center
        screen.blit(Surf, Rect)
        pygame.display.flip()


def getWord():
    print("get word")
    # get the word


def generateButtons():
    print("genere buttons")
    # add remove points

    # show/hide word

    # skip word

teamStart = True
needNum = True
needNames = True
numPlayers = 0
players = []

running = True
while running:
    screenColor()

    if teamStart:
        isTeam = checkTeams()
        # These print statements are to check to make sure function works
        if isTeam:
            print("It's a team")
        else:
            print("It's solo")
        teamStart = False
    
    if needNum:
        numPlayers = getNumPlayers()
        # Print statement is to check to make sure function works
        print(numPlayers)
        needNum = False

    if needNames:
        players = addName(numPlayers)
        # Print statement is to check to make sure function works
        print(players)
        screenColor()
        pygame.display.flip()
        needNames = False

    # Display player names
    
    # Get and display player scores

    # Display current actor

    # Get and display current word

    # Display buttons

    # Display 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
