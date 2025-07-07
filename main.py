from src.game_manager import init_game, reset_game
from src.asteroid import Asteroid
from src.player import MainPlayer
from src.utils import *
from src.ui import *
from pygame import *
from config import *
from random import *
import pygame
import os

pygame.init()
tela = display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
display.set_caption('GameProject')

game_data = init_game()
player = game_data["player"]
objectGroup = game_data["object_Group"]
asteroidGroup = game_data["asteroid_group"]
shotGroup = game_data["shot_group"]
player_score = game_data["player_score"]
level = game_data["level"]
difficult = game_data["difficulty"]
asteroid_speed = game_data["asteroid_speed"]
bg = game_data["bg"]
gameloop = True
start_game = False
gameover = False

# Sounds
mixer.music.load(os.path.join(sounds_dir, "GameMusic.mp3"))
mixer.music.play(-1)
mixer.music.set_volume(MUSIC_VOLUME)
shoot = mixer.Sound(os.path.join(sounds_dir, "Shoot.wav"))

timer = 20
clock = time.Clock()

while gameloop:

    clock.tick(FPS)

    if not start_game:
        HUD(tela, pygame.font.Font(FREE_SANS, FONT_SIZE)).draw_message('Press ESC to start', WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, center=True)

    else:
        mixer.music.set_volume(MUSIC_VOLUME + 0.02)

        if not gameover:
            objectGroup.update()

            timer += 1
            if timer > 30:
                timer = 0
                if random() < 0.35:
                    newAsteroid = Asteroid(objectGroup, asteroidGroup, speed=asteroid_speed)

            if check_collision(player, asteroidGroup):
                print('Game Over!')
                gameover = True

            if check_shot_collision(shotGroup, asteroidGroup):
                player_score += 1
                difficult += 1
                
            if difficult == 10:
                asteroid_speed += 1
                difficult = 0
                level += 1
                print('Dificuldade Aumentada!')


        objectGroup.draw(tela)
        
        # display score
        HUD(tela, pygame.font.Font(FREE_SANS, FONT_SIZE)).draw_score(player_score)
        HUD(tela, pygame.font.Font(FREE_SANS, FONT_SIZE)).draw_level(level)

        if gameover:
            HUD(tela, pygame.font.Font(FREE_SANS, FONT_SIZE)).draw_message('Game Over! Press R to Restart', WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, center=True)

    for event in pygame.event.get():
        if event.type == QUIT:
            gameloop = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                start_game = True
            if event.key == K_r and gameover:
                player = reset_game(game_data)
                player_score = game_data["player_score"]
                level = game_data["level"]
                difficult = game_data["difficulty"]
                asteroid_speed = game_data["asteroid_speed"]
                start_game = True
                gameover = False
            if event.key == K_SPACE and not gameover and start_game:
                player.shoot(objectGroup, shotGroup, shoot)


    display.update()
