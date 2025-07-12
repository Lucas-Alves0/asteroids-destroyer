from src.ui import *
from pygame import *
from config import *
import pygame

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

game_paused = False

button_y = SCREEN_HEIGHT // 2
start_button = Button(screen, frame=0, center=True, pos=(SCREEN_WIDTH // 2, button_y - 100), scale=5)
options_button = Button(screen, frame=1, center=True, pos=(SCREEN_WIDTH // 2, button_y), scale=5)
exit_button = Button(screen, frame=2, center=True, pos=(SCREEN_WIDTH // 2, button_y + 100), scale=5)

run = True
while run:

    screen.fill((52, 78, 91))

    if not game_paused:
        HUD(screen, pygame.font.SysFont(ARIAL_BLACK, 40)).draw_message("Press SPACE to pause", WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, center=True)
    else:
        start_button.draw()
        options_button.draw()
        exit_button.draw()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == 1:
                if start_button.rect.collidepoint(event.pos):
                    game_paused = False
                elif options_button.rect.collidepoint(event.pos):
                    print("Options clicked")
                elif exit_button.rect.collidepoint(event.pos):
                    run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()