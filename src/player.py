from pygame import sprite, image, key, K_w, K_s
from src.utils import *
from src.shot import *
from config import *
import os


class MainPlayer(sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        sheet = image.load(os.path.join(player_dir, "spaceship_concepts.png")).convert_alpha()
        self.image = get_frame(sheet, 0, 0)
        self.rect = self.image.get_rect(topleft=PLAYER_START_POS)
        self.last_shot_time = 0

        self.speed = 0
        self.accelerate = PLAYER_ACCELERATION

    def update(self, *args):
        keys = key.get_pressed()

        if keys[K_w] or keys[K_UP]:
            self.speed -= self.accelerate
        elif keys[K_s] or keys[K_DOWN]:
            self.speed += self.accelerate
        else:
            self.speed *= 0.92

        self.rect.y += self.speed

        self.speed = clamp(self.speed, -PLAYER_MAX_SPEED, PLAYER_MAX_SPEED)
        self.rect.y += self.speed
        self.rect.y = clamp(self.rect.y, 0, SCREEN_HEIGHT - self.rect.height) # Limite vertical

    def shoot(self, all_sprites, shot_group, sound):
        now = pygame.time.get_ticks()
        if now - self.last_shot_time > 400:  # 400 ms cooldown
            sound.play()
            shot = Shot(all_sprites, shot_group)
            shot.rect.center = self.rect.center + pygame.math.Vector2(32, 0)
            self.last_shot_time = now
            return shot
