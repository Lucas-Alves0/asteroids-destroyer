import pygame

# Tela
SCREEN_WIDTH = 840
SCREEN_HEIGHT = 480
FPS = 60

# Sounds
MUSIC_VOLUME = 0.05
SFX_VOLUME = 0.05

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Jogador
PLAYER_START_POS = (SCREEN_WIDTH * 0.05, SCREEN_HEIGHT // 2)
PLAYER_ACCELERATION = 0.3
PLAYER_SIZE = (96, 96)
PLAYER_MAX_SPEED = 8
PLAYER_FRAME_WIDTH = 64
PLAYER_FRAME_HEIGHT = 44

# Tiro
SHOT_SPEED = 6
SHOT_SIZE = (24, 9)

# Asteroides
ASTEROID_SPEED = 1
ASTEROID_SIZE = (70, 70)

# Fontes
FONT_SIZE = 22
pygame.font.init()
FREE_SANS = 'freesansbold.ttf'
ARIAL_BLACK = 'arialblack.ttf'

# assets paths
import os

asset_dir = os.path.dirname(os.path.abspath(__file__))
bg_dir = os.path.join(asset_dir, "assets", "background")
player_dir = os.path.join(asset_dir, "assets", "ships")
shot_dir = os.path.join(asset_dir, "assets", "shoot")
asteroid_dir = os.path.join(asset_dir, "assets", "enemies")
sounds_dir = os.path.join(asset_dir, "assets", "sounds")
