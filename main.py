from src.asteroid import Asteroid
from src.player import MainPlayer
from src.game_manager import init_game, reset_game
from src.leaderboard import *
from src.difficulty import *
from src.utils import *
from src.menu import *
from src.ui import *
from src.auth_ui import AuthUI
from src.main_menu import MainMenu
from src.profile_screen import ProfileScreen
from src.settings_screen import SettingsScreen
from src.leaderboard_screen import LeaderboardScreen
from src.player_registration import PlayerRegistration
from config import *
import random
import pygame
import os
import time

pygame.init()
tela = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Asteroids Destroyer')
clock = pygame.time.Clock()

# Estados do jogo
class GameState:
    AUTH = "auth"
    MAIN_MENU = "main_menu"
    PLAYING = "playing"
    GAME_OVER = "game_over"
    PAUSED = "paused"
    PROFILE = "profile"
    SETTINGS = "settings"
    LEADERBOARD = "leaderboard"

current_state = GameState.AUTH

# Inicializar sistemas
player_reg = PlayerRegistration()
auth_ui = AuthUI(tela)
main_menu = MainMenu(tela, player_reg)
profile_screen = ProfileScreen(tela, player_reg)
settings_screen = SettingsScreen(tela, player_reg)
leaderboard_screen = LeaderboardScreen(tela, player_reg)

# Variáveis do jogo
game_data = None
player = None
objectGroup = None
asteroidGroup = None
shotGroup = None
player_score = 0
level = 1
difficult = 0
asteroid_speed = ASTEROID_SPEED
bg = None
start_game = False
gameover = False

# Sons
pygame.mixer.music.load(os.path.join(sounds_dir, "GameMusic.mp3"))
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(MUSIC_VOLUME)
shoot = pygame.mixer.Sound(os.path.join(sounds_dir, "Shoot.wav"))

# Timer e tutorial
timer = 20
tutorial_timer = 0
show_tutorial = True
game_start_time = 0

gameloop = True

def init_game_session():
    """Inicializa uma nova sessão de jogo"""
    global game_data, player, objectGroup, asteroidGroup, shotGroup, player_score, level, difficult, asteroid_speed, bg, game_start_time
    
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
    game_start_time = time.time()

def reset_game_session():
    """Reseta a sessão de jogo atual"""
    global player, player_score, level, difficult, asteroid_speed, gameover, show_tutorial, tutorial_timer
    
    if game_data is not None:
        player = reset_game(game_data)
        player_score = game_data["player_score"]
        level = game_data["level"]
        difficult = game_data["difficulty"]
        asteroid_speed = game_data["asteroid_speed"]
        gameover = False
        show_tutorial = True
        tutorial_timer = 0

def update_player_stats():
    """Atualiza estatísticas do jogador"""
    if player_reg.current_player and game_start_time > 0:
        playtime = int(time.time() - game_start_time)
        player_reg.update_player_stats(player_score, playtime)

while gameloop:
    clock.tick(FPS)
    
    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT:
            gameloop = False
    
    # Gerenciar estados
    if current_state == GameState.AUTH:
        result = auth_ui.handle_events(events)
        if result == "MAIN_MENU":
            current_state = GameState.MAIN_MENU
        auth_ui.update()
        auth_ui.draw()
    
    elif current_state == GameState.MAIN_MENU:
        result = main_menu.handle_events(events)
        if result == "PLAY":
            init_game_session()
            current_state = GameState.PLAYING
        elif result == "PROFILE":
            current_state = GameState.PROFILE
        elif result == "SETTINGS":
            current_state = GameState.SETTINGS
        elif result == "LEADERBOARD":
            current_state = GameState.LEADERBOARD
        elif result == "AUTH":
            current_state = GameState.AUTH
        main_menu.draw()
    
    elif current_state == GameState.PROFILE:
        result = profile_screen.handle_events(events)
        if result == "MAIN_MENU":
            current_state = GameState.MAIN_MENU
        profile_screen.draw()
    
    elif current_state == GameState.SETTINGS:
        result = settings_screen.handle_events(events)
        if result == "MAIN_MENU":
            current_state = GameState.MAIN_MENU
        settings_screen.draw()
    
    elif current_state == GameState.LEADERBOARD:
        result = leaderboard_screen.handle_events(events)
        if result == "MAIN_MENU":
            current_state = GameState.MAIN_MENU
        leaderboard_screen.draw()
    
    elif current_state == GameState.PLAYING:
        # Tutorial
        if show_tutorial:
            tutorial_timer += clock.get_time()
            if tutorial_timer > 5000:  # 5 segundos
                show_tutorial = False
        
        # Aumentar volume da música gradualmente
        pygame.mixer.music.set_volume(MUSIC_VOLUME + 0.02)
        
        if not gameover and objectGroup is not None:
            objectGroup.update()
            
            # Spawn de asteroides
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
            
            # Verificar colisões
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
        
        # Desenhar elementos do jogo
        if objectGroup is not None:
            objectGroup.draw(tela)
        
        # Tutorial
        if show_tutorial and (tutorial_timer // 500) % 2 == 0:
            HUD(tela, pygame.font.Font(FREE_SANS, FONT_SIZE)).draw_message(
                'W/S para mover / CIMA ou BAIXO | ESPAÇO para atirar',
                WHITE,
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2,
                center=True
            )
        
        # HUD
        HUD(tela, pygame.font.Font(FREE_SANS, FONT_SIZE)).draw_score(player_score)
        HUD(tela, pygame.font.Font(FREE_SANS, FONT_SIZE)).draw_level(level)
        
        # Game Over
        if gameover:
            update_player_stats()
            current_state = GameState.GAME_OVER
    
    elif current_state == GameState.GAME_OVER:
        # Tela de game over
        tela.fill(BLACK)
        
        # Título
        font = pygame.font.Font(FREE_SANS, 36)
        title = font.render("GAME OVER", True, RED)
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, 100))
        tela.blit(title, title_rect)
        
        # Pontuação
        score_font = pygame.font.Font(FREE_SANS, 24)
        score_text = score_font.render(f"Pontuação: {player_score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH//2, 150))
        tela.blit(score_text, score_rect)
        
        # Level
        level_text = score_font.render(f"Level: {level}", True, WHITE)
        level_rect = level_text.get_rect(center=(SCREEN_WIDTH//2, 180))
        tela.blit(level_text, level_rect)
        
        # Botões
        button_font = pygame.font.Font(FREE_SANS, 20)
        
        # Botão jogar novamente
        play_again_button = pygame.Rect(SCREEN_WIDTH//2 - 100, 250, 200, 50)
        pygame.draw.rect(tela, GREEN, play_again_button)
        play_text = button_font.render("JOGAR NOVAMENTE", True, BLACK)
        play_rect = play_text.get_rect(center=play_again_button.center)
        tela.blit(play_text, play_rect)
        
        # Botão menu principal
        menu_button = pygame.Rect(SCREEN_WIDTH//2 - 100, 320, 200, 50)
        pygame.draw.rect(tela, BLUE, menu_button)
        menu_text = button_font.render("MENU PRINCIPAL", True, WHITE)
        menu_rect = menu_text.get_rect(center=menu_button.center)
        tela.blit(menu_text, menu_rect)
        
        # Verificar cliques
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_again_button.collidepoint(event.pos):
                        reset_game_session()
                        current_state = GameState.PLAYING
                    elif menu_button.collidepoint(event.pos):
                        current_state = GameState.MAIN_MENU
    
    # Input do jogo
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and current_state == GameState.PLAYING and player is not None:
                player.shoot(objectGroup, shotGroup, shoot)
            elif event.key == pygame.K_ESCAPE:
                if current_state == GameState.PLAYING:
                    update_player_stats()
                    current_state = GameState.MAIN_MENU
    
    pygame.display.update()

pygame.quit()
