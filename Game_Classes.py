from pygame import *
from random import *

class MainPlayer(sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = image.load(r"C:\Users\lucas.paula_kovi\VSCodeProjects\MyOwnProjects\asteroids_destroy\game_assets\data\Player.png")
        self.image = transform.scale(self.image, [100, 95])
        self.rect = Rect([50, 50, 100, 70])

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


class Asteroid(sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = image.load(r"C:\Users\lucas.paula_kovi\VSCodeProjects\MyOwnProjects\asteroids_destroy\game_assets\data\Asteroid.png")
        self.image = transform.scale(self.image, [70, 70])
        self.rect = Rect([50, 50, 70, 70])

        self.rect.x = 840 + randint(1, 490)
        self.rect.y = randint(1, 360)
        self.speed = 1 + random() * 2

    def update(self, *args):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()

class Shot(sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = image.load(r"C:\Users\lucas.paula_kovi\VSCodeProjects\MyOwnProjects\asteroids_destroy\game_assets\data\Shot.png")
        self.image = transform.scale(self.image, [50, 50])
        self.rect = Rect([50, 50, 50, 50])
        self.speed = 4

    def update(self, *args):
        self.rect.x += self.speed

        if self.rect.left > 840:
            self.kill()
