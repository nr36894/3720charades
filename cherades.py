import pygame
import random
import math
import time
import json
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
                pygame.quit()
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
        Surf = font.render('Enter Number of Players:', True, (255, 255, 255))
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
    player = []
    currP = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
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
                        currP+=1
                        if len(player) == numP:
                            return player
                    name = ""
        screenColor()
        Surf = font.render('Enter Name {}:'.format(currP), True, (255, 255, 255))
        Rect = Surf.get_rect()
        Rect.midtop = (400, 100)
        screen.blit(Surf, Rect)
        Surf = font.render(name, True, (255, 255, 255))
        Rect = Surf.get_rect()
        Rect.center = screen.get_rect().center
        screen.blit(Surf, Rect)
        pygame.display.flip()

def getWordList():
    wordList = api.words(rel_gen='thing', max=200)
    json_str = json.dumps(wordList)
    wordList = json.loads(json_str)
    return wordList


def getWord(wordList):
    word = (wordList[0]['word'])
    return word


def gameDisplay(word):
    screenColor()
    Surf = font.render(word, True, (255, 255, 255))
    Rect = Surf.get_rect()
    Rect.center = screen.get_rect().center
    screen.blit(Surf, Rect)
    pygame.display.flip()
    return(word)



def generateButtons():
    print("generate buttons")
    # add remove points

    # show/hide word

    # skip word

def displayNames():
    print("display names")


teamStart = True
needNum = True
needNames = True
needWord = True
needWordList = True
numPlayers = 0
players = []

running = True
while running:
    screenColor()

    if needNum:
        numPlayers = getNumPlayers()
        # Print statement is to check to make sure function works
        print(numPlayers)
        needNum = False

    if needNames:
        players = addName(numPlayers)
        # Print statement is to check to make sure function works
        print(players)
        needNames = False

    # Display player names
    
    # Get and display player scores

    # Display current actor

    # Generate a list of words
    if needWordList:
        wordList = getWordList()
        # Debug print statement
        print(wordList)
        needWordList = False

    # Get and display current word
    if needWord:
        word = getWord(wordList)
        # Debug print statement
        print(word)
        needWord = False
    # Display buttons

    # Display
    gameDisplay(word)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
