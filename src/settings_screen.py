import pygame
from config import *
from src.player_registration import PlayerRegistration
from src.ui_enhancements import GradientBackground, AnimatedButton, GlowingText, StarField

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
        
        # Elementos visuais
        self.background = GradientBackground(screen)
        self.star_field = StarField(screen)
        self.title_text = GlowingText("CONFIGURAÇÕES", 32, (255, 255, 255), SCREEN_WIDTH//2, 60, center=True)
        
        # Botões animados
        self.back_button = AnimatedButton(50, 50, 120, 40, "VOLTAR", (0, 100, 200), (0, 150, 255))
        self.save_button = AnimatedButton(SCREEN_WIDTH - 170, 50, 120, 40, "SALVAR", (0, 150, 0), (0, 200, 0))
        
        # Sliders
        self.music_slider = Slider(200, 150, 300, 20, 0.0, 1.0, 0.5)
        self.sfx_slider = Slider(200, 220, 300, 20, 0.0, 1.0, 0.5)
        
        # Opções de dificuldade
        self.difficulty_options = ['Fácil', 'Normal', 'Difícil']
        self.current_difficulty = 1  # Normal
        self.difficulty_buttons = []
        for i, option in enumerate(self.difficulty_options):
            x = 200 + i * 120
            self.difficulty_buttons.append(AnimatedButton(x, 300, 100, 40, option, (100, 100, 100), (150, 150, 150)))
        
        # Outras opções
        self.fullscreen_button = AnimatedButton(200, 380, 200, 40, "TELA CHEIA", (100, 100, 100), (150, 150, 150))
        self.fullscreen_enabled = False
        
        self.vsync_button = AnimatedButton(200, 440, 200, 40, "VSYNC", (100, 100, 100), (150, 150, 150))
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
                    if self.back_button.rect.collidepoint(event.pos):
                        return "MAIN_MENU"
                    elif self.save_button.rect.collidepoint(event.pos):
                        self.save_settings()
                        return "MAIN_MENU"
                    elif self.fullscreen_button.rect.collidepoint(event.pos):
                        self.fullscreen_enabled = not self.fullscreen_enabled
                    elif self.vsync_button.rect.collidepoint(event.pos):
                        self.vsync_enabled = not self.vsync_enabled
                    
                    # Verificar botões de dificuldade
                    for i, button in enumerate(self.difficulty_buttons):
                        if button.rect.collidepoint(event.pos):
                            self.current_difficulty = i
            
            # Handle sliders and animated buttons
            self.music_slider.handle_event(event)
            self.sfx_slider.handle_event(event)
            self.back_button.handle_event(event)
            self.save_button.handle_event(event)
            self.fullscreen_button.handle_event(event)
            self.vsync_button.handle_event(event)
            for button in self.difficulty_buttons:
                button.handle_event(event)
        
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
        
        # Atualizar e desenhar botões
        self.back_button.update()
        self.back_button.draw(self.screen)
        
        self.save_button.update()
        self.save_button.draw(self.screen)
        
        # Seção de Áudio
        audio_title = self.font.render("ÁUDIO", True, WHITE)
        self.screen.blit(audio_title, (50, 120))
        
        self.music_slider.draw(self.screen, "Volume da Música")
        self.sfx_slider.draw(self.screen, "Volume dos Efeitos")
        
        # Seção de Jogo
        game_title = self.font.render("JOGO", True, WHITE)
        self.screen.blit(game_title, (50, 270))
        
        # Atualizar e desenhar botões de dificuldade
        for i, button in enumerate(self.difficulty_buttons):
            button.update()
            button.draw(self.screen)
        
        # Outras opções
        other_title = self.font.render("OUTRAS OPÇÕES", True, WHITE)
        self.screen.blit(other_title, (50, 350))
        
        # Atualizar e desenhar botões de opções
        self.fullscreen_button.update()
        self.fullscreen_button.draw(self.screen)
        
        self.vsync_button.update()
        self.vsync_button.draw(self.screen)
        
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