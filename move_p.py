import pygame

def movement1(player_red, player_vel, player_v, width, height):
    player_red.x += player_vel
    if player_red.left <= 0:
        player_red.left = 0
    if player_red.right >= width//2:
        player_red.right = width//2

    player_red.y += player_v
    if player_red.top <= height//12:
        player_red.top = height//12
    if player_red.bottom >= height:
        player_red.bottom = height

def movement2(player_blue, player_speed, player_s, width, height):
    player_blue.x += player_speed
    if player_blue.left <= width//2:
        player_blue.left = width//2
    if player_blue.right >= width:
        player_blue.right = width

    player_blue.y += player_s
    if player_blue.top <= height//12:
        player_blue.top = height//12
    if player_blue.bottom >= height:
        player_blue.bottom = height

def life(red_hp, blue_hp, width, screen):
    font = pygame.font.SysFont('comicsans', 50)
    text = font.render(str(red_hp), 1, 'white')
    screen.blit(text, (width//5, -8))

    font = pygame.font.SysFont('comicsans', 50)
    text = font.render(str(blue_hp), 1, 'white')
    screen.blit(text, (width-width//5, -8))