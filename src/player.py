from pygame import *
import os

asset_dir = os.path.dirname(os.path.dirname(__file__))
ships_dir = os.path.join(asset_dir, "assets", "ships")

class MainPlayer(sprite.Sprite):
    def __init__(self, *groups, skin="Spaceship_move0.png"):
        super().__init__(*groups)

        image_path = os.path.join(ships_dir, skin)
        self.image = image.load(image_path).convert_alpha()
        self.image = transform.scale(self.image, [96, 96])
        self.rect = self.image.get_rect(topleft=(96, 96))

        self.speed = 0
        self.accelerate = 0.3

    def update(self, *args):
        keys = key.get_pressed()

        if keys[K_w]:
            self.speed -= self.accelerate
        elif keys[K_s]:
            self.speed += self.accelerate
        else:
            self.speed *= 0.92

        self.rect.y += self.speed

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
            self.speed = 0