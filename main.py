from src.asteroid import Asteroid
from src.player import MainPlayer
from src.game_manager import *
from src.leaderboard import *
from src.difficulty import *
from src.utils import *
from src.menu import *
from src.ui import *
from config import *
import random
import pygame
import os

pygame.init()
tela = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('GameProject')
current_state = GameState.MENU

game_data = init_game()
player = game_data["player"]
objectGroup = game_data["object_group"]
asteroidGroup = game_data["asteroid_group"]
shotGroup = game_data["shot_group"]
player_score = game_data["player_score"]
level = game_data["level"]
difficult = game_data["difficulty"]
asteroid_speed = game_data["asteroid_speed"]
bg = game_data["bg"]
start_button = Button(tela, frame=0, center=True, pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100), scale=5)
exit_button = Button(tela, frame=2, center=True, pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), scale=5)
restart_button = Button(tela, frame=3, center=True, pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT //2 + 100), scale=5)
gameloop = True
start_game = False
gameover = False

# Sounds
pygame.mixer.music.load(os.path.join(sounds_dir, "GameMusic.mp3"))
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(MUSIC_VOLUME)
shoot = pygame.mixer.Sound(os.path.join(sounds_dir, "Shoot.wav"))

timer = 20
tutorial_timer = 0
show_tutorial = True
clock = pygame.time.Clock()

while gameloop:

    clock.tick(FPS)

    if current_state == GameState.PLAYING and show_tutorial:
        tutorial_timer += clock.get_time()
        if tutorial_timer > 5000:  # Show tutorial for 5 seconds
            show_tutorial = False

    if current_state == GameState.MENU:
        start_button.draw()
        exit_button.draw()
        
    elif current_state == GameState.PLAYING:
        pygame.mixer.music.set_volume(MUSIC_VOLUME + 0.02)

        if not gameover:
            objectGroup.update()

            timer += 1
            if timer > 30:
                timer = 0
                if level < 5:
                    if random.random() < 0.35:
                        newAsteroid = Asteroid(objectGroup, asteroidGroup, speed=asteroid_speed)

                elif level >= 5:
                    spawn_chance = 0.35 + (level * 0.02)
                    if random.random() < min(spawn_chance, 0.8):
                        newAsteroid = Asteroid(objectGroup, asteroidGroup, speed=asteroid_speed + random.uniform(0, level * 0.2), diagonal=allow_diagonal(level) and random.random() < 0.7)

            if check_collision(player, asteroidGroup):
                gameover = True

            if check_shot_collision(shotGroup, asteroidGroup):
                player_score += 1
                difficult += 1
                
            if difficult == 10:
                asteroid_speed += 1
                difficult = 0
                level += 1
                print(f"Dificuldade aumentada!")


        objectGroup.draw(tela)

        if show_tutorial and (tutorial_timer // 500) % 2 == 0:
            HUD(tela, pygame.font.Font(FREE_SANS, FONT_SIZE)).draw_message(
                'W/S para mover / CIMA ou BAIXO | ESPAÇO para atirar',
                WHITE,
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2,
                center=True
        )

        # display score
        HUD(tela, pygame.font.Font(FREE_SANS, FONT_SIZE)).draw_score(player_score)
        HUD(tela, pygame.font.Font(FREE_SANS, FONT_SIZE)).draw_level(level)

        if gameover and is_highest_score(player_score):
            current_state = GameState.GAME_OVER
            name = get_name_input(tela, pygame.font.Font(FREE_SANS, FONT_SIZE)).strip()
            add_score(name, player_score)
            leaderboard = load_leaderboard()

    elif current_state == GameState.GAME_OVER:
        y = 35
        HUD(tela, pygame.font.Font(FREE_SANS, FONT_SIZE)).draw_message(
            "Leaderboard",
            WHITE,
            10,
            10
        )
        HUD(tela, pygame.font.Font(FREE_SANS, FONT_SIZE)).draw_message(
            "____________",
            WHITE,
            10,
            12
        )
        for entry in leaderboard:
            msg = f"{entry['name']}: {entry['score']}"
            HUD(tela, pygame.font.Font(FREE_SANS, FONT_SIZE)).draw_message(
                msg,
                WHITE,
                10,
                y
            )
            y += 25
        restart_button.draw()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if current_state == GameState.MENU:
                    if start_button.rect.collidepoint(event.pos):
                        current_state = GameState.PLAYING
                    elif exit_button.rect.collidepoint(event.pos):
                        gameloop = False
                     
                if current_state == GameState.GAME_OVER:
                    if restart_button.rect.collidepoint(event.pos):
                        player = reset_game(game_data)
                        player_score = game_data["player_score"]
                        level = game_data["level"]
                        difficult = game_data["difficulty"]
                        asteroid_speed = game_data["asteroid_speed"]
                        current_state = GameState.PLAYING
                        start_game = True
                        gameover = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and current_state == GameState.PLAYING:
                player.shoot(objectGroup, shotGroup, shoot)

        if event.type == pygame.QUIT:
            gameloop = False


    pygame.display.update()
