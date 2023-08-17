import pygame, sys

pygame.font.init()

blue_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2

def handle_bullets(bullets_red, bullets_blue, red, blue):
    for bullet in bullets_red:
        pygame.draw.rect(screen, white, bullet)
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

def movement1():
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

def movement2():
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

def life():
    font = pygame.font.SysFont('comicsans', 50)
    text = font.render(str(red_hp), 1, 'white')
    screen.blit(text, (width//5, -5))

    font = pygame.font.SysFont('comicsans', 50)
    text = font.render(str(blue_hp), 1, 'white')
    screen.blit(text, (width-width//5, -5))

def message():
    if red_hp!=0 and blue_hp !=0: return
    if red_hp == 0 :
        font = pygame.font.SysFont('comicsans', 90)
        text = font.render('Blue Wins!', 1, 'white')
        screen.blit(text, ( width//2 - text.get_width()//2 , height//2 - text.get_height()//2 ))
        return
    if blue_hp == 0 :
        font = pygame.font.SysFont('comicsans', 90)
        text = font.render('Red Wins!', 1, 'white')
        screen.blit(text, ( width//2 - text.get_width()//2 , height//2 - text.get_height()//2 ))
        return

clock = pygame.time.Clock()

width, height = 900, 700
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("pew pew pew")

player_red = pygame.Rect(width//4, height//2, 40, 40)
player_blue = pygame.Rect(width*3//4, height//2, 40, 40)

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

bg_color = pygame.Color('grey12')
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                blue_hp = 5
                bullets_blue.clear()
                red_hp = 5
                bullets_red.clear()

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
                bullet = pygame.Rect(player_red.x + player_red.width//2, player_red.y + player_red.height//2, 15, 10)
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
                bullet = pygame.Rect(player_blue.x + player_blue.width//2, player_blue.y + player_blue.height//2, 15, 10)
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

        if event.type == blue_hit:
            if blue_hp>0 :
                blue_hp -= 1 
            else: 
                blue_hp = 0 
        if event.type == red_hit:
            if red_hp >0:
                red_hp -= 1 
            else: 
                red_hp = 0

    movement1()
    movement2()

    screen.fill(bg_color)

    handle_bullets(bullets_red, bullets_blue, player_red, player_blue)

    pygame.draw.rect(screen, 'grey', (0, 0, width, height//12))

    life()

    pygame.draw.rect(screen, red, player_red)
    pygame.draw.rect(screen, blue, player_blue)

    message()

    pygame.display.flip()
    clock.tick(60)
