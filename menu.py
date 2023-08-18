import pygame,sys

def menu(screen, width, height, current_screen, bg_color):
    button_width = 200
    button_height = 50
    button_x = (width - button_width) // 2
    button_y = (height - button_height) // 2

# Create a button rectangle
    button1 = pygame.Rect(button_x, button_y, button_width, button_height)
    font= pygame.font.SysFont('comicsans',30)
    while current_screen==0:

        screen.fill(bg_color)
        pygame.draw.rect(screen, 'grey', button1)
        text = font.render("Start PvP", True, 'white')
        text_start = text.get_rect(center=button1.center)
        screen.blit(text, text_start)

        x,y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and button1.collidepoint(x,y):
                return 1
        
        pygame.display.flip()