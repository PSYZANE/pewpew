import pygame, os, sys
from _thread import *
from move_p import movement1, movement2, life

pygame.font.init()

clock = pygame.time.Clock()

def handle_bullets(screen, bullets_red, bullets_blue, red, blue, bullet_vel, red_hit, blue_hit):
    for bullet in bullets_red:
        pygame.draw.rect(screen, 'white', bullet)
        bullet.x += bullet_vel
        if blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(blue_hit))
            bullets_red.remove(bullet)
        if bullet.x > 910:
            bullets_red.remove(bullet)
    
    for bullet in bullets_blue:
        pygame.draw.rect(screen, 'yellow', bullet)
        bullet.x -= bullet_vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            bullets_blue.remove(bullet)
        if bullet.x < -10:
            bullets_blue.remove(bullet)

def message(screen, width, height,red_hp, blue_hp):
    if red_hp!=0 and blue_hp !=0: return
    if red_hp == 0 :
        font = pygame.font.SysFont('comicsans', 90)
        text = font.render('Blue Wins!', 1, 'white')
        screen.blit(text, ( width//2 - text.get_width()//2 , height//2 - text.get_height()//2 ))
        return
    elif blue_hp == 0 :
        font = pygame.font.SysFont('comicsans', 90)
        text = font.render('Red Wins!', 1, 'white')
        screen.blit(text, ( width//2 - text.get_width()//2 , height//2 - text.get_height()//2 ))
        return
    


def pvp(screen, width, height, current_screen):
    animation_frames = []
    frame_index=0
    for i in range(1,10):
        frame_filename = os.path.join("pewpew/assets/bg", f"Starry_background{i}.png")
        frame_image = pygame.image.load(frame_filename)
        frame_image = pygame.transform.scale(frame_image,(frame_image.get_width()*1.79,frame_image.get_height()*1.79))
        animation_frames.append(frame_image)

    blue_hit = pygame.USEREVENT + 1
    red_hit = pygame.USEREVENT + 2

    red_hp = 5
    blue_hp = 5

    bullets_red=[]
    bullets_blue=[]
    max_bullet = 5
    bullet_vel = 7

    player_vel = 0
    player_v = 0
    player_speed = 0
    player_s = 0


    red = (255, 0, 0)
    blue = (0, 0, 255)
    player_red = pygame.Rect(width//4, height//2, 40, 40)
    player_blue = pygame.Rect(width*3//4, height//2, 40, 40)

    while current_screen == 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #restart the game  ------------------------------------------------------
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    blue_hp = 5
                    bullets_blue.clear()
                    red_hp = 5
                    bullets_red.clear()
                if event.key == pygame.K_ESCAPE:
                    return 0

            # controls of player red  ------------------------------------------------
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player_vel += 7
                if event.key == pygame.K_a:
                    player_vel -= 7
                if event.key == pygame.K_s:
                    player_v += 7
                if event.key == pygame.K_w:
                    player_v -= 7
                if event.key == pygame.K_SPACE and len(bullets_red) < max_bullet:
                    bullet = pygame.Rect(player_red.x + player_red.width//2, player_red.y + player_red.height//2, 15, 5)
                    bullets_red.append(bullet)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player_vel -= 7
                if event.key == pygame.K_a:
                    player_vel += 7 
                if event.key == pygame.K_s:
                    player_v -= 7
                if event.key == pygame.K_w:
                    player_v += 7 

            # controls of player blue  -------------------------------------------------
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_speed -= 7
                if event.key == pygame.K_RIGHT:
                    player_speed += 7
                if event.key == pygame.K_UP:
                    player_s -= 7
                if event.key == pygame.K_DOWN:
                    player_s += 7
                if event.key == pygame.K_RCTRL and len(bullets_blue) < max_bullet:
                    bullet = pygame.Rect(player_blue.x + player_blue.width//2, player_blue.y + player_blue.height//2, 15, 5)
                    bullets_blue.append(bullet)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player_speed += 7
                if event.key == pygame.K_RIGHT:
                    player_speed -= 7 
                if event.key == pygame.K_UP:
                    player_s += 7
                if event.key == pygame.K_DOWN:
                    player_s -= 7 

            # collisions ----------------------------------------------------------------
            if event.type == blue_hit:
                if blue_hp>0 and red_hp==0:
                    blue_hp=blue_hp
                elif blue_hp>0 :
                    blue_hp -= 1 
                else: 
                    blue_hp = 0 
            if event.type == red_hit:
                if red_hp>=0 and blue_hp==0:
                    red_hp=red_hp
                elif red_hp >0:
                    red_hp -= 1 
                else: 
                    red_hp = 0

        start_new_thread(movement1, (player_red, player_vel, player_v, width, height))
        start_new_thread(movement2, (player_blue, player_speed, player_s, width, height))

        screen.blit(animation_frames[frame_index], (-60, height//12))
        frame_index = (frame_index + 1) % len(animation_frames)

        start_new_thread(handle_bullets, (screen, bullets_red, bullets_blue, player_red, player_blue, bullet_vel, red_hit, blue_hit))

        pygame.draw.rect(screen, 'grey', (0, 0, width, height//12))

        life(red_hp, blue_hp, width, screen)

        pygame.draw.rect(screen, red, player_red)
        pygame.draw.rect(screen, blue, player_blue)

        message(screen, width, height,red_hp, blue_hp)

        pygame.display.flip()
        clock.tick(60)