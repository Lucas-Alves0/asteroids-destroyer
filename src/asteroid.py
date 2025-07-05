from pygame import *
from random import *
import os

asset_dir = os.path.dirname(os.path.dirname(__file__))
asteroid_dir = os.path.join(asset_dir, "assets", "enemies")

class Asteroid(sprite.Sprite):
    def __init__(self, *groups, speed):
        super().__init__(*groups)
        
        self.image = image.load(os.path.join(asteroid_dir, "Asteroid.png")).convert_alpha()
        self.image = transform.scale(self.image, [70, 70])
        self.rect = Rect([50, 50, 70, 70])

        self.rect.x = 840 + randint(1, 490)
        self.rect.y = randint(1, 360)
        self.speed = speed + random() * 2

    def update(self, *args):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()