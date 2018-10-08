import pygame
from pygame.locals import *
import os
import sys
import math
import random

pygame.init()

#CODE FOR DISPLAY
W, H = 800, 480
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('MoneyBags Scroller')
pygame.display.set_icon(pygame.image.load(os.path.join('images','gameicon.png')))
clock = pygame.time.Clock()

#Code to retrieve background image from files
bg = pygame.image.load(os.path.join('images','BGLoop.png')).convert()
bgX = 0
bgX2 = bg.get_width()

#mal_counter = 0


#CREATE ATTRIBUTES OF CARL (place image in variable, set start position on screen, width(carlwid) and height (carlht)
carl_image = pygame.transform.scale(pygame.image.load(os.path.join('images', 'creditkarl.png')), (100,100))
carl_pos = [20,200]
carlwid, carlht = 236, 336


#CREATE ATTRIBUTES OF MALWARE
malware_image = pygame.transform.scale(pygame.image.load(os.path.join('images','malware.png')), (50,50))
#mal_position = [800, random.randint(30,430)]
#malware = win.blit(malware_image, mal_position)
#mal_timer = 0
#mal_active = []


class malware():
    img = malware_image
    def __init__(self, x, y, width, height):
        self.x = 300
        self.y = random.randint(30,430)
        self.width = width
        self.height = height
        self.hitbox = (x, y, width, height)
        self.count = 0


    def draw(self, win):
        self.hitbox(self.x + 5, self.y + 5, self.width - 10, self.height)
        if self.count >= 8:
            self.count = 0
        win.blit(self.img, (self.x, self.y))
        self.count += 1
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

#mal_add = malware(800, random.randint(30,430), 128, 128)

#bug = malware(300,300,128,128)



#Function to refresh display during gameplay
def redrawWindow():
    win.blit(bg, (bgX,0))
    win.blit(bg, (bgX2,0))
    win.blit(carl_image, carl_pos)
    #win.blit(mal_active, mal_position)
    #bug.draw()
    pygame.display.update()


#Code for RUNNING GAME
pygame.time.set_timer(USEREVENT + 1, 500)
speed = 30
run = True

#Process all code within while loop while run = True
while run:
    redrawWindow()

    #Parameters to make background scroll
    bgX -= 1.4
    bgX2 -= 1.4
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()
    
    for event in pygame.event.get():

        #Close window if X pressed
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()


        #Increse loop speed of background
        if event.type == USEREVENT + 1:
            speed += 1


        #Close window if Escape key is pressed
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            run = False
            pygame.quit()
            quit()


    #MAP MOVEMENTS TO KEYBOARD
    keys = [False,False]

    #If Key Pressed (to move Carl)
    if event.type == pygame.KEYDOWN:
        if event.key == K_UP or event.key == K_w:
            keys[0] = True
        elif event.key == K_DOWN or event.key == K_s:
            keys[1] = True

    #If Key Unpressed (STOP moving Carl)
    elif event.type == pygame.KEYUP:
        if event.key == K_UP or event.key == K_w:
            keys[0] = False
        elif event.key == K_DOWN or event.key == K_s:
            keys[1] = False

    #Amount of movement
    if keys[0] == True:
        carl_pos[1] -= 1
    elif keys[1] == True:
        carl_pos[1] += 1


"""
    #Add malware to appear on screen:
    if mal_counter < 8:
        mal_active.append(malware_image)
        #mal_timer += 
    elif mal_counter

    for bug in mal_active:
        if bug.x < 0:
            mal_active.pop(bug)
"""



"""

    #Be able to restart if Win
    winMode = ()
    elif winMode and event.key == K_r:
        return

"""
                                        
clock.tick(speed)
