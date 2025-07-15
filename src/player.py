from pygame import sprite, image, key, K_w, K_s, K_a, K_d, K_LEFT, K_RIGHT
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

        self.speed_y = 0
        self.speed_x = 0
        self.accelerate = PLAYER_ACCELERATION

    def update(self, *args):
        keys = key.get_pressed()

        # Movimento vertical
        if keys[K_w] or keys[K_UP]:
            self.speed_y -= self.accelerate
        elif keys[K_s] or keys[K_DOWN]:
            self.speed_y += self.accelerate
        else:
            self.speed_y *= 0.92

        # Movimento horizontal
        if keys[K_a] or keys[K_LEFT]:
            self.speed_x -= self.accelerate
        elif keys[K_d] or keys[K_RIGHT]:
            self.speed_x += self.accelerate
        else:
            self.speed_x *= 0.92

        # Aplicar velocidades
        self.rect.y += int(self.speed_y)
        self.rect.x += int(self.speed_x)

        # Limitar velocidades
        self.speed_y = clamp(self.speed_y, -PLAYER_MAX_SPEED, PLAYER_MAX_SPEED)
        self.speed_x = clamp(self.speed_x, -PLAYER_MAX_SPEED, PLAYER_MAX_SPEED)
        
        # Limitar posição na tela
        self.rect.y = clamp(self.rect.y, 0, SCREEN_HEIGHT - self.rect.height)
        self.rect.x = clamp(self.rect.x, 0, SCREEN_WIDTH - self.rect.width)

    def shoot(self, all_sprites, shot_group, sound):
        now = pygame.time.get_ticks()
        if now - self.last_shot_time > 400:  # 400 ms cooldown
            sound.play()
            shot = Shot(all_sprites, shot_group)
            shot.rect.center = (self.rect.centerx + 32, self.rect.centery)
            self.last_shot_time = now
            return shot
