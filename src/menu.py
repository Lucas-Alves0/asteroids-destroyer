from src.utils import *
from pygame import *
from config import *
import os

class Button:
    def __init__(self, tela, frame=0, center=False, pos=(100, 100), scale=5):
        self.tela = tela
        self.center = center
        self.pos = pos
        self.image = pygame.image.load(os.path.join(buttons_dir, "new_menu.png")).convert_alpha()
        self.frame_index = frame

        frame_image = get_frame(self.image, 0, self.frame_index, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.image = pygame.transform.scale(frame_image, (BUTTON_WIDTH * scale, BUTTON_HEIGHT * scale))
        self.rect = self.image.get_rect()

        if self.center:
            self.rect.center = self.pos
        else:
            self.rect.topleft = self.pos

    def draw(self):
        self.tela.blit(self.image, self.rect)