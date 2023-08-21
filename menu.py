import pygame,sys

def menu(screen, width, height, current_screen, bg_color):
    button_width = 200
    button_height = 50
    button_x = (width - button_width) // 2
    button_y = (height - button_height) // 2
    button2_y = height//3 - button_height//2

# Create a button rectangle
    button1 = pygame.Rect(button_x, button_y, button_width, button_height)
    button2 = pygame.Rect(button_x, button2_y, button_width, button_height)
    
    while current_screen==0:

        screen.fill(bg_color)
        font= pygame.font.SysFont('comicsans',30)
        pygame.draw.rect(screen, 'grey', button1)
        text = font.render("Start PvP", True, 'white')
        text_start = text.get_rect(center=button1.center)
        screen.blit(text, text_start)

        pygame.draw.rect(screen, 'grey', button2)
        text = font.render("Start PvE", True, 'white')
        text_start = text.get_rect(center=button2.center)
        screen.blit(text, text_start)

        x,y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and button1.collidepoint(x,y):
                if event.button == 1:
                    return 1
            if event.type == pygame.MOUSEBUTTONDOWN and button2.collidepoint(x,y):
                if event.button == 1:
                    return 2
        
        pygame.display.flip()