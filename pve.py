import pygame, math, sys
import random

clock = pygame.time.Clock()

class Bullet:
    def __init__(self, x, y, width, height, speed, targetx, targety):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        angle = math.atan2(targety-y, targetx-x)
        self.dx = math.cos(angle)*speed
        self.dy = math.sin(angle)*speed
        self.x=0
        self.y=0

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.x += int(self.x)
        self.rect.y += int(self.y)

    def collided(self, other_rect):
        return self.rect.colliderect(other_rect)
    
    def draw(self, screen):
        pygame.draw.ellipse(screen, 'white', self.rect)

    def limit(self):
        # Check if b is out of bounds  --------------
        if self.rect.x > 910 or self.rect.x < 0 or self.rect.y > 710 or self.rect.y < 0:
            return True

class Enemy:
    def __init__(self, width, height, speed, targetx, targety):
        x = random.randint(0, 900)
        y = random.randint(100, 700)
        self.rect = pygame.Rect(x, y, width, height)
        angle = math.atan2(targety-y, targetx-x)
        self.dx = math.cos(angle)*speed
        self.dy = math.sin(angle)*speed
        self.x=0
        self.y=0

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.x += int(self.x)
        self.rect.y += int(self.y)

    def collided(self, other_rect):
        return self.rect.colliderect(other_rect)
    
    def draw(self, screen):
        pygame.draw.ellipse(screen, 'red', self.rect)

    def limit(self):
        # Check if b is out of bounds  --------------
        if self.rect.x > 910 or self.rect.x < 0 or self.rect.y > 710 or self.rect.y < 0:
            return True


def pve(screen, width, height, current_screen, bg_color):

    mode=1
    
    player_width = 40
    player_height = 40
    hp=5
    
    score = 0

    enemies = []
    enemy_speed = 0.07

    bullets=[]
    max_bullet = 5
    bullet_vel = 2
    bullet_cooldown = 100  # Time between bullet shots in milliseconds
    last_bullet_time = pygame.time.get_ticks()

    player_vel = 0
    player_v = 0
    player = pygame.Rect(width//2-20, height//2-20, player_width, player_height)  
    font= pygame.font.SysFont('comicsans', 50)

    while current_screen==2:

        screen.fill(bg_color)

        if len(enemies) < 5:
            x, y = player.x,player.y
            e = Enemy(player_width, player_height, enemy_speed, x, y)
            enemies.append(e)
    
        for e in enemies:
            e.draw(screen)
            e.move()
            if e.limit():
                enemies.remove(e)
            if e.collided(player) and hp!=0:
                enemies.remove(e)
                if hp>0:
                    hp-=1

        if hp==0:
            text = font.render("your score is "+str(score), True, 'white')
            screen.blit(text, (width//2-text.get_width()//2 , height//2-text.get_height()//2))
            enemy_speed = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 0
                if event.key == pygame.K_BACKSPACE:
                    score = 0
                    hp=5
                    enemy_speed = 0.07
                    bullets.clear()
                    enemies.clear()
                
                if event.key == pygame.K_1:
                    mode = 1
                if event.key == pygame.K_2:
                    mode = 2

                if event.key == pygame.K_d:
                    player_vel += 7
                if event.key == pygame.K_a:
                    player_vel -= 7
                if event.key == pygame.K_s:
                    player_v += 7
                if event.key == pygame.K_w:
                    player_v -= 7

                if event.key == pygame.K_SPACE and len(bullets) < max_bullet and mode==2:
                    for e in enemies:
                        x,y = e.rect.x, e.rect.y
                        b = Bullet(player.centerx, player.centery, 10, 10, bullet_vel/5, x, y)
                        bullets.append(b)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player_vel -= 7
                if event.key == pygame.K_a:
                    player_vel += 7 
                if event.key == pygame.K_s:
                    player_v -= 7
                if event.key == pygame.K_w:
                    player_v += 7

        current_time = pygame.time.get_ticks()           
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and len(bullets) < 1 and mode==1 and current_time - last_bullet_time > bullet_cooldown:
            last_bullet_time = current_time
            for e in enemies:
                if len(bullets) < 1:
                    x,y = e.rect.x, e.rect.y
                    b = Bullet(player.centerx, player.centery, 10, 10, bullet_vel*2, x, y)
                    bullets.append(b)

        # player animation regarding movement  -----------
        player.x += player_vel
        if player.left <= 0:
            player.left = 0
        if player.right >= width:
            player.right = width

        player.y += player_v
        if player.top <= height//12:
            player.top = height//12
        if player.bottom >= height:
            player.bottom = height
        
        #  handling bullets --------------------------------
        for b in bullets:
            b.draw(screen)
            b.move()
            if b.limit():
                bullets.remove(b)
            for e in enemies:
                if b.collided(e.rect) and hp!=0:
                    score+=10
                    enemies.remove(e)
        
        pygame.draw.rect(screen, 'grey', player)
        text = font.render("life : "+str(hp), True, 'white')
        screen.blit(text, (width//2-text.get_width()//2 , -8))

        pygame.display.flip()
        clock.tick(60)
    