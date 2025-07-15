import pygame
from config import *
from src.player_registration import PlayerRegistration

class MainMenu:
    def __init__(self, screen, player_reg):
        self.screen = screen
        self.player_reg = player_reg
        self.font = pygame.font.Font(FREE_SANS, 24)
        self.small_font = pygame.font.Font(FREE_SANS, 18)
        self.title_font = pygame.font.Font(FREE_SANS, 36)
        
        # Botões do menu principal
        button_width = 250
        button_height = 60
        center_x = SCREEN_WIDTH // 2
        start_y = 200
        
        self.play_button = pygame.Rect(center_x - button_width//2, start_y, button_width, button_height)
        self.profile_button = pygame.Rect(center_x - button_width//2, start_y + 80, button_width, button_height)
        self.settings_button = pygame.Rect(center_x - button_width//2, start_y + 160, button_width, button_height)
        self.leaderboard_button = pygame.Rect(center_x - button_width//2, start_y + 240, button_width, button_height)
        self.logout_button = pygame.Rect(center_x - button_width//2, start_y + 320, button_width, button_height)
        
        # Cores dos botões
        self.button_colors = {
            'play': GREEN,
            'profile': BLUE,
            'settings': YELLOW,
            'leaderboard': PURPLE,
            'logout': RED
        }
        
        self.button_texts = {
            'play': 'JOGAR',
            'profile': 'PERFIL',
            'settings': 'CONFIGURAÇÕES',
            'leaderboard': 'RANKING',
            'logout': 'SAIR'
        }
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.play_button.collidepoint(event.pos):
                        return "PLAY"
                    elif self.profile_button.collidepoint(event.pos):
                        return "PROFILE"
                    elif self.settings_button.collidepoint(event.pos):
                        return "SETTINGS"
                    elif self.leaderboard_button.collidepoint(event.pos):
                        return "LEADERBOARD"
                    elif self.logout_button.collidepoint(event.pos):
                        self.player_reg.logout_player()
                        return "AUTH"
        return None
    
    def draw(self):
        self.screen.fill(BLACK)
        
        # Título
        title = self.title_font.render("ASTEROIDS DESTROYER", True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, 80))
        self.screen.blit(title, title_rect)
        
        # Informações do jogador
        if self.player_reg.current_player:
            player_data = self.player_reg.get_current_player_data()
            if player_data:
                welcome_text = f"Bem-vindo, {self.player_reg.current_player}!"
                welcome_surface = self.small_font.render(welcome_text, True, WHITE)
                welcome_rect = welcome_surface.get_rect(center=(SCREEN_WIDTH//2, 130))
                self.screen.blit(welcome_surface, welcome_rect)
                
                # Estatísticas rápidas
                stats_text = f"Melhor pontuação: {player_data['highest_score']} | Jogos: {player_data['total_games']}"
                stats_surface = self.small_font.render(stats_text, True, (200, 200, 200))
                stats_rect = stats_surface.get_rect(center=(SCREEN_WIDTH//2, 160))
                self.screen.blit(stats_surface, stats_rect)
        
        # Botões
        buttons = [
            (self.play_button, 'play'),
            (self.profile_button, 'profile'),
            (self.settings_button, 'settings'),
            (self.leaderboard_button, 'leaderboard'),
            (self.logout_button, 'logout')
        ]
        
        for button, key in buttons:
            pygame.draw.rect(self.screen, self.button_colors[key], button)
            pygame.draw.rect(self.screen, WHITE, button, 2)
            
            text = self.font.render(self.button_texts[key], True, BLACK if key == 'play' else WHITE)
            text_rect = text.get_rect(center=button.center)
            self.screen.blit(text, text_rect) 