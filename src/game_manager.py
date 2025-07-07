from src.player import MainPlayer
from pygame.sprite import Group
from config import *
import pygame
import os


def init_game():
    object_Group = Group()
    asteroid_group = Group()
    shot_group = Group()

    bg = pygame.sprite.Sprite(object_Group)
    bg.image = pygame.image.load(os.path.join(bg_dir, "Cenario.png")).convert()
    bg.image = pygame.transform.scale(bg.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg.rect = bg.image.get_rect()

    player = MainPlayer(object_Group)

    return {
        "player": player,
        "object_Group": object_Group,
        "asteroid_group": asteroid_group,
        "shot_group": shot_group,
        "bg": bg,
        "player_score": 0,
        "level": 1,
        "difficulty": 0,
        "asteroid_speed": ASTEROID_SPEED
    }

def reset_game(game_data):

    game_data["object_Group"].empty()
    game_data["asteroid_group"].empty()
    game_data["shot_group"].empty()

    bg = pygame.sprite.Sprite(game_data["object_Group"])
    bg.image = pygame.image.load(os.path.join(bg_dir, "Cenario.png")).convert()
    bg.image = pygame.transform.scale(bg.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg.rect = bg.image.get_rect()
    game_data["bg"] = bg

    player = MainPlayer(game_data["object_Group"])
    game_data["player"] = player

    game_data["player_score"] = 0
    game_data["level"] = 1
    game_data["difficulty"] = 0
    game_data["asteroid_speed"] = ASTEROID_SPEED

    return player