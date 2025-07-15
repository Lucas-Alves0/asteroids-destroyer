import pygame
import math
import random
from config import *

class GradientBackground:
    def __init__(self, screen):
        self.screen = screen
        self.time = 0
        self.colors = [
            (20, 20, 40),   # Azul escuro
            (40, 20, 60),   # Roxo escuro
            (60, 20, 40),   # Vermelho escuro
            (20, 40, 60),   # Azul médio
        ]
        self.current_color = 0
        self.transition_speed = 0.02
    
    def update(self):
        self.time += self.transition_speed
        if self.time >= 1.0:
            self.time = 0
            self.current_color = (self.current_color + 1) % len(self.colors)
    
    def draw(self):
        # Criar gradiente animado
        color1 = self.colors[self.current_color]
        color2 = self.colors[(self.current_color + 1) % len(self.colors)]
        
        for y in range(SCREEN_HEIGHT):
            ratio = y / SCREEN_HEIGHT
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
            pygame.draw.line(self.screen, (r, g, b), (0, y), (SCREEN_WIDTH, y))

class AnimatedButton:
    def __init__(self, x, y, width, height, text, color, hover_color, font_size=20):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.current_color = color
        self.font = pygame.font.Font(FREE_SANS, font_size)
        self.hover = False
        self.animation_speed = 0.1
        self.glow_alpha = 0
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.hover = True
            else:
                self.hover = False
    
    def update(self):
        target_color = self.hover_color if self.hover else self.color
        self.current_color = self.lerp_color(self.current_color, target_color, self.animation_speed)
        
        if self.hover:
            self.glow_alpha = min(255, self.glow_alpha + 15)
        else:
            self.glow_alpha = max(0, self.glow_alpha - 15)
    
    def lerp_color(self, color1, color2, factor):
        return tuple(int(color1[i] + (color2[i] - color1[i]) * factor) for i in range(3))
    
    def draw(self, screen):
        # Desenhar brilho quando hover
        if self.glow_alpha > 0:
            glow_surface = pygame.Surface((self.rect.width + 20, self.rect.height + 20))
            glow_surface.set_alpha(self.glow_alpha)
            glow_surface.fill(self.hover_color)
            screen.blit(glow_surface, (self.rect.x - 10, self.rect.y - 10))
        
        # Desenhar botão com gradiente
        gradient_surface = pygame.Surface((self.rect.width, self.rect.height))
        for i in range(self.rect.height):
            ratio = i / self.rect.height
            color = self.lerp_color(self.current_color, (max(0, self.current_color[0] - 30), 
                                   max(0, self.current_color[1] - 30), 
                                   max(0, self.current_color[2] - 30)), ratio)
            pygame.draw.line(gradient_surface, color, (0, i), (self.rect.width, i))
        
        screen.blit(gradient_surface, self.rect)
        
        # Borda
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
        
        # Texto
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

class ParticleSystem:
    def __init__(self):
        self.particles = []
    
    def add_particle(self, x, y, color=(255, 255, 255)):
        self.particles.append({
            'x': x,
            'y': y,
            'vx': random.uniform(-2, 2),
            'vy': random.uniform(-2, 2),
            'life': 60,
            'max_life': 60,
            'color': color,
            'size': random.randint(2, 4)
        })
    
    def update(self):
        for particle in self.particles[:]:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 1
            
            if particle['life'] <= 0:
                self.particles.remove(particle)
    
    def draw(self, screen):
        for particle in self.particles:
            alpha = int(255 * (particle['life'] / particle['max_life']))
            color = (*particle['color'], alpha)
            
            # Criar superfície com alpha
            particle_surface = pygame.Surface((particle['size'] * 2, particle['size'] * 2))
            particle_surface.set_alpha(alpha)
            particle_surface.fill(color)
            screen.blit(particle_surface, (particle['x'] - particle['size'], 
                                         particle['y'] - particle['size']))

class AnimatedText:
    def __init__(self, text, font_size, color, x, y, center=False):
        self.text = text
        self.font = pygame.font.Font(FREE_SANS, font_size)
        self.color = color
        self.x = x
        self.y = y
        self.center = center
        self.alpha = 0
        self.target_alpha = 255
        self.animation_speed = 5
        
    def update(self):
        if self.alpha < self.target_alpha:
            self.alpha = min(self.target_alpha, self.alpha + self.animation_speed)
    
    def draw(self, screen):
        if self.alpha > 0:
            text_surface = self.font.render(self.text, True, self.color)
            text_surface.set_alpha(self.alpha)
            
            if self.center:
                text_rect = text_surface.get_rect(center=(self.x, self.y))
            else:
                text_rect = text_surface.get_rect(topleft=(self.x, self.y))
            
            screen.blit(text_surface, text_rect)

class ProgressBar:
    def __init__(self, x, y, width, height, value=0, max_value=100):
        self.rect = pygame.Rect(x, y, width, height)
        self.value = value
        self.max_value = max_value
        self.target_value = value
        self.animation_speed = 0.1
    
    def set_value(self, value):
        self.target_value = value
    
    def update(self):
        self.value += (self.target_value - self.value) * self.animation_speed
    
    def draw(self, screen):
        # Fundo
        pygame.draw.rect(screen, (50, 50, 50), self.rect)
        pygame.draw.rect(screen, (100, 100, 100), self.rect, 2)
        
        # Barra de progresso
        if self.max_value > 0:
            progress_width = int((self.value / self.max_value) * self.rect.width)
            if progress_width > 0:
                progress_rect = pygame.Rect(self.rect.x, self.rect.y, progress_width, self.rect.height)
                
                # Gradiente na barra
                for i in range(progress_rect.height):
                    ratio = i / progress_rect.height
                    color = (
                        int(0 + (100 - 0) * ratio),
                        int(150 + (255 - 150) * ratio),
                        int(0 + (100 - 0) * ratio)
                    )
                    pygame.draw.line(screen, color, 
                                   (progress_rect.x, progress_rect.y + i),
                                   (progress_rect.x + progress_rect.width, progress_rect.y + i))

class GlowingText:
    def __init__(self, text, font_size, color, x, y, center=False):
        self.text = text
        self.font = pygame.font.Font(FREE_SANS, font_size)
        self.color = color
        self.x = x
        self.y = y
        self.center = center
        self.glow_alpha = 0
        self.glow_direction = 1
    
    def update(self):
        self.glow_alpha += 3 * self.glow_direction
        if self.glow_alpha >= 100:
            self.glow_direction = -1
        elif self.glow_alpha <= 0:
            self.glow_direction = 1
    
    def draw(self, screen):
        # Glow effect
        if self.glow_alpha > 0:
            glow_surface = self.font.render(self.text, True, self.color)
            glow_surface.set_alpha(self.glow_alpha)
            
            if self.center:
                glow_rect = glow_surface.get_rect(center=(self.x, self.y))
            else:
                glow_rect = glow_surface.get_rect(topleft=(self.x, self.y))
            
            # Desenhar múltiplas camadas para efeito de brilho
            for offset in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
                screen.blit(glow_surface, (glow_rect.x + offset[0], glow_rect.y + offset[1]))
        
        # Texto principal
        text_surface = self.font.render(self.text, True, self.color)
        if self.center:
            text_rect = text_surface.get_rect(center=(self.x, self.y))
        else:
            text_rect = text_surface.get_rect(topleft=(self.x, self.y))
        
        screen.blit(text_surface, text_rect)

class StarField:
    def __init__(self, screen):
        self.screen = screen
        self.stars = []
        self.generate_stars()
    
    def generate_stars(self):
        for _ in range(100):
            self.stars.append({
                'x': random.randint(0, SCREEN_WIDTH),
                'y': random.randint(0, SCREEN_HEIGHT),
                'speed': random.uniform(0.5, 2.0),
                'size': random.randint(1, 3),
                'brightness': random.randint(100, 255)
            })
    
    def update(self):
        for star in self.stars:
            star['y'] += star['speed']
            if star['y'] > SCREEN_HEIGHT:
                star['y'] = 0
                star['x'] = random.randint(0, SCREEN_WIDTH)
    
    def draw(self):
        for star in self.stars:
            color = (star['brightness'], star['brightness'], star['brightness'])
            pygame.draw.circle(self.screen, color, (int(star['x']), int(star['y'])), star['size']) 