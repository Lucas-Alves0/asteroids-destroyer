from pygame import sprite, image, transform, Rect
from random import randint, random
from config import *
import os

class Asteroid(sprite.Sprite):
    def __init__(self, *groups, speed):
        super().__init__(*groups)
        
        self.image = image.load(os.path.join(asteroid_dir, "Asteroid.png"))
        self.image = transform.scale(self.image, ASTEROID_SIZE)
        self.rect = Rect([50, 50, *ASTEROID_SIZE])

        self.rect.x = SCREEN_WIDTH + randint(1, SCREEN_HEIGHT)
        self.rect.y = randint(1, 360)
        self.speed = speed + random() * 2

    def update(self, *args):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()