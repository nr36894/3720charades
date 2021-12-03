import pygame
import random
import math
import time
import json
from datamuse import datamuse
from pygame.constants import K_1
from collections import Counter
api = datamuse.Datamuse()
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
counter, counterText = 20, '20'.rjust(3)
font = pygame.font.SysFont('Consolas', 30)

pygame.time.set_timer(pygame.USEREVENT, 1000)
pygame.display.set_caption('Let\'s Play Charades')

# Scren Dimensions
width = screen.get_width()
height = screen.get_height()

# Button One Values
buttonOneX = 500
buttonOneY = 10
buttonOneW = 140
buttonOneH = 40

#Button Two Values
buttonTwoX = 500
buttonTwoY = 60
buttonTwoW = 140
buttonTwoH = 40

# Next Word Button
nwButtonX = 410
nwButtonY = 350
nwButtonW = 155
nwButtonH = 40

# Skip Word Button
skipButtonX = 234
skipButtonY = 350
skipButtonW = 155
skipButtonH = 40

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
gray = pygame.Color(170, 170, 170)
green = pygame.Color(0, 255, 0)

# Important variables
running = True
points = [0,0]

# Background color of screen
def screenColor():
    screen.fill(black)

def generateButtons():
    buttonOneText = font.render('+ Point' , True , black)

    if buttonOneX <= mouse[0] <= buttonOneX + buttonOneW and buttonOneY <= mouse[1] <= buttonOneY + buttonOneH:
         pygame.draw.rect(screen, gray, [buttonOneX, buttonOneY, buttonOneW, buttonOneH])
    else:
        pygame.draw.rect(screen, white, [buttonOneX, buttonOneY, buttonOneW, buttonOneH])

    screen.blit(buttonOneText, (buttonOneX, buttonOneY))

    buttonTwoText = font.render('+ Point' , True , black)

    if buttonTwoX <= mouse[0] <= buttonTwoX + buttonTwoW and buttonTwoY <= mouse[1] <= buttonTwoY + buttonTwoH:
         pygame.draw.rect(screen, gray, [buttonTwoX, buttonTwoY, buttonTwoW, buttonTwoH])
    else:
        pygame.draw.rect(screen, white, [buttonTwoX, buttonTwoY, buttonTwoW, buttonTwoH])

    screen.blit(buttonTwoText, (buttonTwoX, buttonTwoY))

    newButtonText = font.render('Next Word' , True , black)

    if nwButtonX <= mouse[0] <= nwButtonX + nwButtonW and nwButtonY <= mouse[1] <= nwButtonY + nwButtonH:
         pygame.draw.rect(screen, gray, [nwButtonX, nwButtonY, nwButtonW, nwButtonH])
    else:
        pygame.draw.rect(screen, white, [nwButtonX, nwButtonY, nwButtonW, nwButtonH])

    screen.blit(newButtonText, (nwButtonX, nwButtonY))

    skipButtonText = font.render('Skip Word' , True , black)

    if skipButtonX <= mouse[0] <= skipButtonX + skipButtonW and skipButtonY <= mouse[1] <= skipButtonY + skipButtonH:
         pygame.draw.rect(screen, gray, [skipButtonX, skipButtonY, skipButtonW, skipButtonH])
    else:
        pygame.draw.rect(screen, white, [skipButtonX, skipButtonY, skipButtonW, skipButtonH])

    screen.blit(skipButtonText, (skipButtonX, skipButtonY))


def showScore(choice, turn):
    # Team 1
    text1 = ""
    text2 = ""

    # Score shown during game play with each team's points
    # Scores will be shown in upper left hand corner
    if choice == 1:
        text1 = "Team 1 Score: " + str(points[0])
        text2 = "Team 2 Score: " + str(points[1])
        if turn == 1:
            t1surf = font.render(text1, True, green)
            t2surf = font.render(text2, True, white)
        elif turn == 2:
            t1surf = font.render(text1, True, white)
            t2surf = font.render(text2, True, green)

        t1rect = t1surf.get_rect()
        t1rect.topleft = (140, 10)
        screen.blit(t1surf, t1rect)
        t2rect = t2surf.get_rect()
        t2rect.topleft = (140, 60)
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
        t1surf = font.render(text1, True, white)
        t1rect = t1surf.get_rect()
        t1rect.midtop = (400, 120)
        screen.blit(t1surf, t1rect)

def getWordList():
    wordList = api.words(rel_gen='thing', max=20)
    json_str = json.dumps(wordList)
    wordList = json.loads(json_str)
    return wordList


def getWord(wordList):
    word = (wordList[random.randint(0, 10)]['word'])
    return word

def displayWord(word):
    screenColor()
    Surf = font.render(word, True, (255, 255, 255))
    Rect = Surf.get_rect()
    Rect.center = screen.get_rect().center
    screen.blit(Surf, Rect)


needWord = True
generateList = False
gameOver = False
turn = 1
while running:
    screenColor()

    mouse = pygame.mouse.get_pos()

    # Display current actor


    # Generate List of Words
    if not generateList:
        wordList = getWordList()
        generateList = True

    # Get and display current word
    if needWord:
        word = getWord(wordList);
        needWord = False

    if not gameOver:
        displayWord(word)

    # Manages game state
    if counter > 0:
        showScore(1, turn) # To show the score
        generateButtons()
        screen.blit(font.render("Seconds Remaining: " + counterText, True, white), (140, 110))
    else:
        showScore(0, None) # To show winner/tie
        gameOver = True

    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
            counter -= 1
            counterText = str(counter).rjust(3)
        elif event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and counter > 0:
            if buttonOneX <= mouse[0] <= buttonOneX + buttonOneW and 10 <= mouse[1] <= buttonOneY + buttonOneH:
                points[0] += 1
            elif buttonTwoX <= mouse[0] <= buttonTwoX + buttonTwoW and 10 <= mouse[1] <= buttonTwoY + buttonTwoH:
                points[1] += 1
            elif nwButtonX <= mouse[0] <= nwButtonX + nwButtonW and nwButtonY <= mouse[1] <= nwButtonY + nwButtonH:
                needWord = True;
                counter = 20
                counterText = str(counter).rjust(3)
                if turn == 1:
                    turn = 2
                elif turn == 2:
                    turn = 1
            elif skipButtonX <= mouse[0] <= skipButtonX + skipButtonW and skipButtonY <= mouse[1] <= skipButtonY + skipButtonH:
                needWord = True;
                counter = 20
                counterText = str(counter).rjust(3)

    clock.tick(60)
    pygame.display.flip()