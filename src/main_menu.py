import pygame
from config import *
from src.player_registration import PlayerRegistration
from src.ui_enhancements import GradientBackground, AnimatedButton, GlowingText, StarField

class MainMenu:
    def __init__(self, screen, player_reg):
        self.screen = screen
        self.player_reg = player_reg
        self.font = pygame.font.Font(FREE_SANS, 24)
        self.small_font = pygame.font.Font(FREE_SANS, 18)
        self.title_font = pygame.font.Font(FREE_SANS, 36)
        
        # Elementos visuais
        self.background = GradientBackground(screen)
        self.star_field = StarField(screen)
        self.title_text = GlowingText("ASTEROIDS DESTROYER", 36, (255, 255, 255), SCREEN_WIDTH//2, 80, center=True)
        
        # Botões animados do menu principal
        button_width = 250
        button_height = 60
        center_x = SCREEN_WIDTH // 2
        start_y = 200
        
        self.play_button = AnimatedButton(center_x - button_width//2, start_y, button_width, button_height, 
                                        "JOGAR", (0, 150, 0), (0, 200, 0))
        self.profile_button = AnimatedButton(center_x - button_width//2, start_y + 80, button_width, button_height, 
                                           "PERFIL", (0, 100, 200), (0, 150, 255))
        self.settings_button = AnimatedButton(center_x - button_width//2, start_y + 160, button_width, button_height, 
                                            "CONFIGURAÇÕES", (200, 150, 0), (255, 200, 0))
        self.leaderboard_button = AnimatedButton(center_x - button_width//2, start_y + 240, button_width, button_height, 
                                               "RANKING", (150, 0, 200), (200, 0, 255))
        self.logout_button = AnimatedButton(center_x - button_width//2, start_y + 320, button_width, button_height, 
                                          "SAIR", (200, 0, 0), (255, 50, 50))
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.play_button.rect.collidepoint(event.pos):
                        return "PLAY"
                    elif self.profile_button.rect.collidepoint(event.pos):
                        return "PROFILE"
                    elif self.settings_button.rect.collidepoint(event.pos):
                        return "SETTINGS"
                    elif self.leaderboard_button.rect.collidepoint(event.pos):
                        return "LEADERBOARD"
                    elif self.logout_button.rect.collidepoint(event.pos):
                        self.player_reg.logout_player()
                        return "AUTH"
            
            # Handle animated buttons
            self.play_button.handle_event(event)
            self.profile_button.handle_event(event)
            self.settings_button.handle_event(event)
            self.leaderboard_button.handle_event(event)
            self.logout_button.handle_event(event)
        
        return None
    
    def draw(self):
        # Desenhar fundo animado
        self.background.update()
        self.background.draw()
        
        # Desenhar campo de estrelas
        self.star_field.update()
        self.star_field.draw()
        
        # Atualizar e desenhar título animado
        self.title_text.update()
        self.title_text.draw(self.screen)
        
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
        
        # Atualizar e desenhar botões animados
        self.play_button.update()
        self.play_button.draw(self.screen)
        
        self.profile_button.update()
        self.profile_button.draw(self.screen)
        
        self.settings_button.update()
        self.settings_button.draw(self.screen)
        
        self.leaderboard_button.update()
        self.leaderboard_button.draw(self.screen)
        
        self.logout_button.update()
        self.logout_button.draw(self.screen) 