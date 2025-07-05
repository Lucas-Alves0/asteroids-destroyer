from pygame import *
from random import *
import os

asset_dir = os.path.dirname(os.path.dirname(__file__))
shoot_dir = os.path.join(asset_dir, "assets", "shoot")

class Shot(sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = image.load(os.path.join(shoot_dir, "Shot_1.png")).convert_alpha()
        self.image = transform.scale(self.image, [24, 9])
        self.rect = Rect([24, 9, 24, 9])
        self.speed = 4

    def update(self, *args):
        self.rect.x += self.speed

        if self.rect.left > 840:
            self.kill()