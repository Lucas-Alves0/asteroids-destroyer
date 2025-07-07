from pygame import *
from config import *


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