import pygame
from config import *
from src.player_registration import PlayerRegistration
from src.ui_enhancements import GradientBackground, AnimatedButton, AnimatedText, GlowingText, StarField

class InputField:
    def __init__(self, x, y, width, height, placeholder="", is_password=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.placeholder = placeholder
        self.is_password = is_password
        self.active = False
        self.font = pygame.font.Font(FREE_SANS, 18)
        self.color = WHITE
        self.active_color = GREEN
        self.placeholder_color = (128, 128, 128)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                return "ENTER"
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_TAB:
                self.active = False
                return "TAB"
            else:
                char = event.unicode
                if char.isprintable() and len(self.text) < 30:
                    self.text += char
        return False
    
    def draw(self, screen):
        color = self.active_color if self.active else self.color
        pygame.draw.rect(screen, color, self.rect, 2)
        
        if self.text:
            display_text = "*" * len(self.text) if self.is_password else self.text
            text_surface = self.font.render(display_text, True, WHITE)
        else:
            text_surface = self.font.render(self.placeholder, True, self.placeholder_color)
        
        text_rect = text_surface.get_rect()
        text_rect.x = self.rect.x + 10
        text_rect.centery = self.rect.centery
        screen.blit(text_surface, text_rect)

class AuthUI:
    def __init__(self, screen):
        self.screen = screen
        self.player_reg = PlayerRegistration()
        self.current_state = "login"  # login, register
        self.message = ""
        self.message_timer = 0
        
        # Elementos visuais
        self.background = GradientBackground(screen)
        self.star_field = StarField(screen)
        self.title_text = GlowingText("ASTEROIDS DESTROYER", 36, (255, 255, 255), SCREEN_WIDTH//2, 80, center=True)
        
        # Campos de login
        self.login_username = InputField(SCREEN_WIDTH//2 - 150, 200, 300, 40, "Nome de usuário")
        self.login_password = InputField(SCREEN_WIDTH//2 - 150, 260, 300, 40, "Senha", is_password=True)
        
        # Campos de registro
        self.register_username = InputField(SCREEN_WIDTH//2 - 150, 180, 300, 40, "Nome de usuário")
        self.register_email = InputField(SCREEN_WIDTH//2 - 150, 240, 300, 40, "Email")
        self.register_password = InputField(SCREEN_WIDTH//2 - 150, 300, 300, 40, "Senha", is_password=True)
        self.register_confirm_password = InputField(SCREEN_WIDTH//2 - 150, 360, 300, 40, "Confirmar senha", is_password=True)
        
        # Botões animados
        self.login_button = AnimatedButton(SCREEN_WIDTH//2 - 100, 320, 200, 50, "ENTRAR", (0, 150, 0), (0, 200, 0))
        self.register_button = AnimatedButton(SCREEN_WIDTH//2 - 100, 420, 200, 50, "CRIAR CONTA", (0, 150, 0), (0, 200, 0))
        self.switch_to_register_button = AnimatedButton(SCREEN_WIDTH//2 - 100, 380, 200, 50, "CRIAR CONTA", (0, 100, 200), (0, 150, 255))
        self.switch_to_login_button = AnimatedButton(SCREEN_WIDTH//2 - 100, 480, 200, 50, "VOLTAR AO LOGIN", (0, 100, 200), (0, 150, 255))
        
        self.font = pygame.font.Font(FREE_SANS, 24)
        self.small_font = pygame.font.Font(FREE_SANS, 18)
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.current_state == "login":
                    if self.login_button.rect.collidepoint(event.pos):
                        success, message = self.player_reg.login_player(
                            self.login_username.text, 
                            self.login_password.text
                        )
                        self.show_message(message, success)
                        if success:
                            return "MAIN_MENU"
                    
                    elif self.switch_to_register_button.rect.collidepoint(event.pos):
                        self.current_state = "register"
                        self.clear_fields()
                
                elif self.current_state == "register":
                    if self.register_button.rect.collidepoint(event.pos):
                        if self.register_password.text != self.register_confirm_password.text:
                            self.show_message("Senhas não coincidem!", False)
                        else:
                            success, message = self.player_reg.register_player(
                                self.register_username.text,
                                self.register_email.text,
                                self.register_password.text
                            )
                            self.show_message(message, success)
                            if success:
                                self.current_state = "login"
                                self.clear_fields()
                    
                    elif self.switch_to_login_button.rect.collidepoint(event.pos):
                        self.current_state = "login"
                        self.clear_fields()
            
            # Handle input fields and animated buttons
            if self.current_state == "login":
                result_username = self.login_username.handle_event(event)
                result_password = self.login_password.handle_event(event)
                
                # Se Enter foi pressionado em qualquer campo, fazer login
                if result_username == "ENTER" or result_password == "ENTER":
                    success, message = self.player_reg.login_player(
                        self.login_username.text, 
                        self.login_password.text
                    )
                    self.show_message(message, success)
                    if success:
                        return "MAIN_MENU"
                
                self.login_button.handle_event(event)
                self.switch_to_register_button.handle_event(event)
            else:
                result_username = self.register_username.handle_event(event)
                result_email = self.register_email.handle_event(event)
                result_password = self.register_password.handle_event(event)
                result_confirm = self.register_confirm_password.handle_event(event)
                
                # Se Enter foi pressionado em qualquer campo, tentar registrar
                if any(result == "ENTER" for result in [result_username, result_email, result_password, result_confirm]):
                    if self.register_password.text != self.register_confirm_password.text:
                        self.show_message("Senhas não coincidem!", False)
                    else:
                        success, message = self.player_reg.register_player(
                            self.register_username.text,
                            self.register_email.text,
                            self.register_password.text
                        )
                        self.show_message(message, success)
                        if success:
                            self.current_state = "login"
                            self.clear_fields()
                
                self.register_button.handle_event(event)
                self.switch_to_login_button.handle_event(event)
        
        return None
    
    def show_message(self, message, success=True):
        self.message = message
        self.message_timer = 120  # 2 segundos a 60 FPS
        self.message_color = GREEN if success else RED
    
    def clear_fields(self):
        self.login_username.text = ""
        self.login_password.text = ""
        self.register_username.text = ""
        self.register_email.text = ""
        self.register_password.text = ""
        self.register_confirm_password.text = ""
    
    def update(self):
        if self.message_timer > 0:
            self.message_timer -= 1
    
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
        
        if self.current_state == "login":
            self.draw_login_screen()
        else:
            self.draw_register_screen()
        
        # Mensagem
        if self.message_timer > 0:
            message_surface = self.small_font.render(self.message, True, self.message_color)
            message_rect = message_surface.get_rect(center=(SCREEN_WIDTH//2, 500))
            self.screen.blit(message_surface, message_rect)
    
    def draw_login_screen(self):
        # Subtítulo
        subtitle = self.small_font.render("Faça login para continuar", True, WHITE)
        subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH//2, 140))
        self.screen.blit(subtitle, subtitle_rect)
        
        # Campos de entrada
        self.login_username.draw(self.screen)
        self.login_password.draw(self.screen)
        
        # Atualizar e desenhar botões animados
        self.login_button.update()
        self.login_button.draw(self.screen)
        
        self.switch_to_register_button.update()
        self.switch_to_register_button.draw(self.screen)
    
    def draw_register_screen(self):
        # Subtítulo
        subtitle = self.small_font.render("Crie sua conta", True, WHITE)
        subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH//2, 140))
        self.screen.blit(subtitle, subtitle_rect)
        
        # Campos de entrada
        self.register_username.draw(self.screen)
        self.register_email.draw(self.screen)
        self.register_password.draw(self.screen)
        self.register_confirm_password.draw(self.screen)
        
        # Atualizar e desenhar botões animados
        self.register_button.update()
        self.register_button.draw(self.screen)
        
        self.switch_to_login_button.update()
        self.switch_to_login_button.draw(self.screen)
    
    def get_current_player(self):
        return self.player_reg.current_player 