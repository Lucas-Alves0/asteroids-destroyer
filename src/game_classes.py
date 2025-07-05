from pygame import *
from random import *

class MainPlayer(sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        # Load the spaceship image
        self.image = image.load(r"C:\Users\lucas.paula_kovi\VSCodeProjects\MyOwnProjects\asteroids_destroy\game_assets\data\Spaceship_move0.png")
        self.image = transform.scale(self.image, [96, 96])
        self.rect = self.image.get_rect()
        self.rect.topleft = [96, 96]

        self.speed = 0
        self.accelerate = 0.3

    def update(self, *args):
        # Get the keys pressed
        keys = key.get_pressed()

        # Check if the keys are pressed

        if keys[K_w]: # If the key W is pressed, the spaceship will move up
            self.speed -= self.accelerate
        elif keys[K_s]: # If the key S is pressed, the spaceship will move down
            self.speed += self.accelerate
        else:
            self.speed *= 0.92 # If key is not pressed, the spaceship will slow down

        self.rect.y += self.speed # Move the spaceship

        # Check if the spaceship is out of the screen

        if self.rect.top < 0: # If the spaceship is out of the screen, the spaceship will be placed at the top of the screen
            self.rect.top = 0
            self.speed = 0
        elif self.rect.bottom > 480: # If the spaceship is out of the screen, the spaceship will be placed at the bottom of the screen
            self.rect.bottom = 480
            self.speed = 0


class Asteroid(sprite.Sprite):
    def __init__(self, *groups, speed):
        super().__init__(*groups)

        self.image = image.load(r"C:\Users\lucas.paula_kovi\VSCodeProjects\MyOwnProjects\asteroids_destroy\assets\enemies\Asteroid.png")
        self.image = transform.scale(self.image, [70, 70])
        self.rect = Rect([50, 50, 70, 70])

        self.rect.x = 840 + randint(1, 490)
        self.rect.y = randint(1, 360)
        self.speed = speed + random() * 2

    def update(self, *args):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()

class Shot(sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = image.load(r"C:\Users\lucas.paula_kovi\VSCodeProjects\MyOwnProjects\asteroids_destroy\assets\data\Shot_1.png")
        self.image = transform.scale(self.image, [24, 9])
        self.rect = Rect([24, 9, 24, 9])
        self.speed = 4

    def update(self, *args):
        self.rect.x += self.speed

        if self.rect.left > 840:
            self.kill()