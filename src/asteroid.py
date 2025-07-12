from pygame import sprite, image, transform, Rect
from random import randint, random
from config import *
import os

class Asteroid(sprite.Sprite):
    def __init__(self, *groups, speed, diagonal=False):
        super().__init__(*groups)
        
        self.image = image.load(os.path.join(asteroid_dir, "Asteroid.png"))
        self.image = transform.scale(self.image, ASTEROID_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = randint(0, SCREEN_HEIGHT - self.rect.height)

        self.speed_x = speed
        self.diagonal = diagonal

        if self.diagonal:
            self.speed_y = randint(-2, 2)
        else:
            self.speed_y = speed = 0

    def update(self, *args):
        self.rect.x -= self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed_y *= -1

        if self.rect.left > SCREEN_WIDTH:
            self.kill()