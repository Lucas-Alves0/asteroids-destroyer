from pygame import sprite, image, transform, Rect
from config import *
import os

class Shot(sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = image.load(os.path.join(shot_dir, "Shot_1.png"))
        self.image = transform.scale(self.image, SHOT_SIZE)
        self.rect = Rect([24, 9, *SHOT_SIZE])
        self.speed = SHOT_SPEED

    def update(self, *args):
        self.rect.x += self.speed

        if self.rect.left > SCREEN_WIDTH:
            self.kill()