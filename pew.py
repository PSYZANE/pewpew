import pygame, sys, os
from menu import menu
from pve import pve
from pvp import pvp

clock = pygame.time.Clock()
current_screen=0

width, height = 900, 700
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("pew pew pew")

bg_color = pygame.Color('grey12')

while True:
    if current_screen == 0:
        current_screen= menu(screen, width, height, current_screen, bg_color)
    
    elif current_screen == 2:
        current_screen= pve(screen, width, height, current_screen, bg_color)
        print("wtf")
    
    elif current_screen == 1:
        current_screen= pvp(screen, width, height, current_screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)