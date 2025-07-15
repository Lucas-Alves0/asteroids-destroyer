import pygame
from config import *
from src.player_registration import PlayerRegistration

class Slider:
    def __init__(self, x, y, width, height, min_val, max_val, initial_val):
        self.rect = pygame.Rect(x, y, width, height)
        self.min_val = min_val
        self.max_val = max_val
        self.value = initial_val
        self.dragging = False
        self.font = pygame.font.Font(FREE_SANS, 16)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            rel_x = event.pos[0] - self.rect.x
            self.value = self.min_val + (rel_x / self.rect.width) * (self.max_val - self.min_val)
            self.value = max(self.min_val, min(self.max_val, self.value))
    
    def draw(self, screen, label):
        # Desenhar label
        label_surface = self.font.render(f"{label}: {self.value:.1f}", True, WHITE)
        screen.blit(label_surface, (self.rect.x, self.rect.y - 25))
        
        # Desenhar slider
        pygame.draw.rect(screen, WHITE, self.rect, 2)
        
        # Desenhar indicador
        indicator_x = self.rect.x + (self.value - self.min_val) / (self.max_val - self.min_val) * self.rect.width
        indicator_rect = pygame.Rect(indicator_x - 5, self.rect.y - 5, 10, self.rect.height + 10)
        pygame.draw.rect(screen, GREEN, indicator_rect)

class SettingsScreen:
    def __init__(self, screen, player_reg):
        self.screen = screen
        self.player_reg = player_reg
        self.font = pygame.font.Font(FREE_SANS, 24)
        self.small_font = pygame.font.Font(FREE_SANS, 18)
        self.title_font = pygame.font.Font(FREE_SANS, 32)
        
        # Botão voltar
        self.back_button = pygame.Rect(50, 50, 120, 40)
        self.save_button = pygame.Rect(SCREEN_WIDTH - 170, 50, 120, 40)
        
        # Sliders
        self.music_slider = Slider(200, 150, 300, 20, 0.0, 1.0, 0.5)
        self.sfx_slider = Slider(200, 220, 300, 20, 0.0, 1.0, 0.5)
        
        # Opções de dificuldade
        self.difficulty_options = ['Fácil', 'Normal', 'Difícil']
        self.current_difficulty = 1  # Normal
        self.difficulty_buttons = []
        for i, option in enumerate(self.difficulty_options):
            x = 200 + i * 120
            self.difficulty_buttons.append(pygame.Rect(x, 300, 100, 40))
        
        # Outras opções
        self.fullscreen_button = pygame.Rect(200, 380, 200, 40)
        self.fullscreen_enabled = False
        
        self.vsync_button = pygame.Rect(200, 440, 200, 40)
        self.vsync_enabled = True
        
        # Carregar configurações atuais
        self.load_current_settings()
    
    def load_current_settings(self):
        player_data = self.player_reg.get_current_player_data()
        if player_data and 'settings' in player_data:
            settings = player_data['settings']
            self.music_slider.value = settings.get('music_volume', 0.5)
            self.sfx_slider.value = settings.get('sfx_volume', 0.5)
            
            difficulty = settings.get('difficulty', 'normal')
            if difficulty == 'easy':
                self.current_difficulty = 0
            elif difficulty == 'normal':
                self.current_difficulty = 1
            else:
                self.current_difficulty = 2
    
    def save_settings(self):
        player_data = self.player_reg.get_current_player_data()
        if player_data:
            if 'settings' not in player_data:
                player_data['settings'] = {}
            
            player_data['settings']['music_volume'] = self.music_slider.value
            player_data['settings']['sfx_volume'] = self.sfx_slider.value
            
            difficulty_map = ['easy', 'normal', 'hard']
            player_data['settings']['difficulty'] = difficulty_map[self.current_difficulty]
            
            self.player_reg.save_players()
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.back_button.collidepoint(event.pos):
                        return "MAIN_MENU"
                    elif self.save_button.collidepoint(event.pos):
                        self.save_settings()
                        return "MAIN_MENU"
                    elif self.fullscreen_button.collidepoint(event.pos):
                        self.fullscreen_enabled = not self.fullscreen_enabled
                    elif self.vsync_button.collidepoint(event.pos):
                        self.vsync_enabled = not self.vsync_enabled
                    
                    # Verificar botões de dificuldade
                    for i, button in enumerate(self.difficulty_buttons):
                        if button.collidepoint(event.pos):
                            self.current_difficulty = i
            
            # Handle sliders
            self.music_slider.handle_event(event)
            self.sfx_slider.handle_event(event)
        
        return None
    
    def draw(self):
        self.screen.fill(BLACK)
        
        # Título
        title = self.title_font.render("CONFIGURAÇÕES", True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, 60))
        self.screen.blit(title, title_rect)
        
        # Botões
        pygame.draw.rect(self.screen, BLUE, self.back_button)
        back_text = self.small_font.render("VOLTAR", True, WHITE)
        back_text_rect = back_text.get_rect(center=self.back_button.center)
        self.screen.blit(back_text, back_text_rect)
        
        pygame.draw.rect(self.screen, GREEN, self.save_button)
        save_text = self.small_font.render("SALVAR", True, BLACK)
        save_text_rect = save_text.get_rect(center=self.save_button.center)
        self.screen.blit(save_text, save_text_rect)
        
        # Seção de Áudio
        audio_title = self.font.render("ÁUDIO", True, WHITE)
        self.screen.blit(audio_title, (50, 120))
        
        self.music_slider.draw(self.screen, "Volume da Música")
        self.sfx_slider.draw(self.screen, "Volume dos Efeitos")
        
        # Seção de Jogo
        game_title = self.font.render("JOGO", True, WHITE)
        self.screen.blit(game_title, (50, 270))
        
        # Botões de dificuldade
        for i, (button, option) in enumerate(zip(self.difficulty_buttons, self.difficulty_options)):
            color = GREEN if i == self.current_difficulty else BLUE
            pygame.draw.rect(self.screen, color, button)
            pygame.draw.rect(self.screen, WHITE, button, 2)
            
            option_text = self.small_font.render(option, True, WHITE)
            option_text_rect = option_text.get_rect(center=button.center)
            self.screen.blit(option_text, option_text_rect)
        
        # Outras opções
        other_title = self.font.render("OUTRAS OPÇÕES", True, WHITE)
        self.screen.blit(other_title, (50, 350))
        
        # Fullscreen
        fullscreen_color = GREEN if self.fullscreen_enabled else BLUE
        pygame.draw.rect(self.screen, fullscreen_color, self.fullscreen_button)
        pygame.draw.rect(self.screen, WHITE, self.fullscreen_button, 2)
        fullscreen_text = self.small_font.render("TELA CHEIA", True, WHITE)
        fullscreen_text_rect = fullscreen_text.get_rect(center=self.fullscreen_button.center)
        self.screen.blit(fullscreen_text, fullscreen_text_rect)
        
        # VSync
        vsync_color = GREEN if self.vsync_enabled else BLUE
        pygame.draw.rect(self.screen, vsync_color, self.vsync_button)
        pygame.draw.rect(self.screen, WHITE, self.vsync_button, 2)
        vsync_text = self.small_font.render("VSYNC", True, WHITE)
        vsync_text_rect = vsync_text.get_rect(center=self.vsync_button.center)
        self.screen.blit(vsync_text, vsync_text_rect)
        
        # Informações
        info_y = 500
        info_texts = [
            "Configurações são salvas automaticamente",
            "Algumas mudanças podem requerer reiniciar o jogo"
        ]
        
        for info in info_texts:
            info_surface = self.small_font.render(info, True, (150, 150, 150))
            self.screen.blit(info_surface, (50, info_y))
            info_y += 25 