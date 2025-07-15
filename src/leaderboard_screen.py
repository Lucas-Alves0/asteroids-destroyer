import pygame
from config import *
from src.leaderboard import load_leaderboard
from src.player_registration import PlayerRegistration

class LeaderboardScreen:
    def __init__(self, screen, player_reg):
        self.screen = screen
        self.player_reg = player_reg
        self.font = pygame.font.Font(FREE_SANS, 24)
        self.small_font = pygame.font.Font(FREE_SANS, 18)
        self.title_font = pygame.font.Font(FREE_SANS, 32)
        
        # Botão voltar
        self.back_button = pygame.Rect(50, 50, 120, 40)
        
        # Categorias do ranking
        self.categories = ['MELHORES PONTUAÇÕES', 'MAIS JOGOS', 'MAIS TEMPO JOGADO']
        self.current_category = 0
        
        # Botões de categoria
        self.category_buttons = []
        for i, category in enumerate(self.categories):
            x = 150 + i * 200
            self.category_buttons.append(pygame.Rect(x, 120, 180, 40))
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.back_button.collidepoint(event.pos):
                        return "MAIN_MENU"
                    
                    # Verificar categorias
                    for i, button in enumerate(self.category_buttons):
                        if button.collidepoint(event.pos):
                            self.current_category = i
        return None
    
    def draw(self):
        self.screen.fill(BLACK)
        
        # Título
        title = self.title_font.render("RANKING GLOBAL", True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, 60))
        self.screen.blit(title, title_rect)
        
        # Botão voltar
        pygame.draw.rect(self.screen, BLUE, self.back_button)
        back_text = self.small_font.render("VOLTAR", True, WHITE)
        back_text_rect = back_text.get_rect(center=self.back_button.center)
        self.screen.blit(back_text, back_text_rect)
        
        # Botões de categoria
        for i, (button, category) in enumerate(zip(self.category_buttons, self.categories)):
            color = GREEN if i == self.current_category else BLUE
            pygame.draw.rect(self.screen, color, button)
            pygame.draw.rect(self.screen, WHITE, button, 2)
            
            # Quebrar texto longo
            if len(category) > 15:
                words = category.split()
                if len(words) > 2:
                    category = '\n'.join([' '.join(words[:2]), ' '.join(words[2:])])
            
            if '\n' in category:
                lines = category.split('\n')
                for j, line in enumerate(lines):
                    line_text = self.small_font.render(line, True, WHITE)
                    line_rect = line_text.get_rect(center=(button.centerx, button.centery - 8 + j * 16))
                    self.screen.blit(line_text, line_rect)
            else:
                category_text = self.small_font.render(category, True, WHITE)
                category_text_rect = category_text.get_rect(center=button.center)
                self.screen.blit(category_text, category_text_rect)
        
        # Conteúdo do ranking
        if self.current_category == 0:
            self.draw_score_ranking()
        elif self.current_category == 1:
            self.draw_games_ranking()
        else:
            self.draw_time_ranking()
    
    def draw_score_ranking(self):
        # Carregar dados de todos os jogadores
        all_players = self.player_reg.players
        
        # Ordenar por melhor pontuação
        sorted_players = sorted(
            all_players.items(),
            key=lambda x: x[1]['highest_score'],
            reverse=True
        )
        
        # Cabeçalho
        header_y = 200
        headers = ["POS", "JOGADOR", "MELHOR PONTUAÇÃO", "TOTAL JOGOS"]
        
        for i, header in enumerate(headers):
            x = 50 + i * 150
            header_surface = self.font.render(header, True, YELLOW)
            self.screen.blit(header_surface, (x, header_y))
        
        # Linha separadora
        pygame.draw.line(self.screen, WHITE, (50, header_y + 30), (SCREEN_WIDTH - 50, header_y + 30), 2)
        
        # Lista de jogadores
        y = header_y + 50
        for pos, (username, data) in enumerate(sorted_players[:10], 1):
            # Posição
            pos_text = self.small_font.render(f"{pos}º", True, WHITE)
            self.screen.blit(pos_text, (50, y))
            
            # Nome do jogador
            name_text = self.small_font.render(username, True, WHITE)
            self.screen.blit(name_text, (200, y))
            
            # Melhor pontuação
            score_text = self.small_font.render(str(data['highest_score']), True, GREEN)
            self.screen.blit(score_text, (350, y))
            
            # Total de jogos
            games_text = self.small_font.render(str(data['total_games']), True, WHITE)
            self.screen.blit(games_text, (500, y))
            
            # Destacar jogador atual
            if username == self.player_reg.current_player:
                pygame.draw.rect(self.screen, GREEN, (45, y - 5, SCREEN_WIDTH - 90, 30), 2)
            
            y += 35
    
    def draw_games_ranking(self):
        # Carregar dados de todos os jogadores
        all_players = self.player_reg.players
        
        # Ordenar por total de jogos
        sorted_players = sorted(
            all_players.items(),
            key=lambda x: x[1]['total_games'],
            reverse=True
        )
        
        # Cabeçalho
        header_y = 200
        headers = ["POS", "JOGADOR", "TOTAL JOGOS", "PONTUAÇÃO MÉDIA"]
        
        for i, header in enumerate(headers):
            x = 50 + i * 150
            header_surface = self.font.render(header, True, YELLOW)
            self.screen.blit(header_surface, (x, header_y))
        
        # Linha separadora
        pygame.draw.line(self.screen, WHITE, (50, header_y + 30), (SCREEN_WIDTH - 50, header_y + 30), 2)
        
        # Lista de jogadores
        y = header_y + 50
        for pos, (username, data) in enumerate(sorted_players[:10], 1):
            # Posição
            pos_text = self.small_font.render(f"{pos}º", True, WHITE)
            self.screen.blit(pos_text, (50, y))
            
            # Nome do jogador
            name_text = self.small_font.render(username, True, WHITE)
            self.screen.blit(name_text, (200, y))
            
            # Total de jogos
            games_text = self.small_font.render(str(data['total_games']), True, BLUE)
            self.screen.blit(games_text, (350, y))
            
            # Pontuação média
            avg_score = data['total_score'] // max(1, data['total_games'])
            avg_text = self.small_font.render(str(avg_score), True, WHITE)
            self.screen.blit(avg_text, (500, y))
            
            # Destacar jogador atual
            if username == self.player_reg.current_player:
                pygame.draw.rect(self.screen, GREEN, (45, y - 5, SCREEN_WIDTH - 90, 30), 2)
            
            y += 35
    
    def draw_time_ranking(self):
        # Carregar dados de todos os jogadores
        all_players = self.player_reg.players
        
        # Ordenar por tempo total jogado
        sorted_players = sorted(
            all_players.items(),
            key=lambda x: x[1]['total_playtime'],
            reverse=True
        )
        
        # Cabeçalho
        header_y = 200
        headers = ["POS", "JOGADOR", "TEMPO TOTAL", "JOGOS/HORA"]
        
        for i, header in enumerate(headers):
            x = 50 + i * 150
            header_surface = self.font.render(header, True, YELLOW)
            self.screen.blit(header_surface, (x, header_y))
        
        # Linha separadora
        pygame.draw.line(self.screen, WHITE, (50, header_y + 30), (SCREEN_WIDTH - 50, header_y + 30), 2)
        
        # Lista de jogadores
        y = header_y + 50
        for pos, (username, data) in enumerate(sorted_players[:10], 1):
            # Posição
            pos_text = self.small_font.render(f"{pos}º", True, WHITE)
            self.screen.blit(pos_text, (50, y))
            
            # Nome do jogador
            name_text = self.small_font.render(username, True, WHITE)
            self.screen.blit(name_text, (200, y))
            
            # Tempo total (formatado)
            total_seconds = data['total_playtime']
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            time_str = f"{hours}h {minutes}m"
            time_text = self.small_font.render(time_str, True, PURPLE)
            self.screen.blit(time_text, (350, y))
            
            # Jogos por hora
            if hours > 0:
                games_per_hour = data['total_games'] / hours
                gph_text = self.small_font.render(f"{games_per_hour:.1f}", True, WHITE)
            else:
                gph_text = self.small_font.render("N/A", True, WHITE)
            self.screen.blit(gph_text, (500, y))
            
            # Destacar jogador atual
            if username == self.player_reg.current_player:
                pygame.draw.rect(self.screen, GREEN, (45, y - 5, SCREEN_WIDTH - 90, 30), 2)
            
            y += 35 