from src.utils import *
from pygame import *
from config import *
import os


class HUD:
    def __init__(self, tela, fonte):
        self.tela = tela
        self.fonte = fonte

    def draw_score(self, score):
        texto = self.fonte.render(f'Score: {score}', True, WHITE)
        self.tela.blit(texto, (10, 10))

    def draw_level(self, level):
        texto = self.fonte.render(f'Level: {level}', True, WHITE)
        self.tela.blit(texto, (SCREEN_WIDTH - 100, 10))

    def draw_message(self, text, color, x, y, center=False):
        message = self.fonte.render(text, True, color)
        if center:
            rect = message.get_rect(center=(x, y))
            self.tela.blit(message, rect)
        else:
            self.tela.blit(message, (x, y))

def get_name_input(tela, font, max_chars=10):
    name = ""
    input_active = True

    while input_active:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    input_active = False
                elif event.key == K_BACKSPACE:
                    name = name[:-1]
                elif len(name) < max_chars:
                    char = event.unicode
                    if char.isalnum() or char in " ._-":
                        name += char

        tela.fill(BLACK)
        msg = font.render("Digite seu nome:", True, WHITE)
        nome_txt = font.render(name + "|", True, WHITE)
        tela.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, 100))
        tela.blit(nome_txt, (SCREEN_WIDTH // 2 - nome_txt.get_width() // 2, 160))
        pygame.display.update()

    return name