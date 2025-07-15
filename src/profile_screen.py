import pygame
from config import *
from datetime import datetime

class ProfileScreen:
    def __init__(self, screen, player_reg):
        self.screen = screen
        self.player_reg = player_reg
        self.font = pygame.font.Font(FREE_SANS, 24)
        self.small_font = pygame.font.Font(FREE_SANS, 18)
        self.title_font = pygame.font.Font(FREE_SANS, 32)
        
        # Botão voltar
        self.back_button = pygame.Rect(50, 50, 120, 40)
        
        # Seções do perfil
        self.sections = ['ESTATÍSTICAS', 'CONQUISTAS', 'HISTÓRICO']
        self.current_section = 0
        
        # Botões de seção
        self.section_buttons = []
        for i, section in enumerate(self.sections):
            x = 200 + i * 200
            self.section_buttons.append(pygame.Rect(x, 120, 150, 40))
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.back_button.collidepoint(event.pos):
                        return "MAIN_MENU"
                    
                    # Verificar seções
                    for i, button in enumerate(self.section_buttons):
                        if button.collidepoint(event.pos):
                            self.current_section = i
        return None
    
    def draw(self):
        self.screen.fill(BLACK)
        
        # Título
        title = self.title_font.render("PERFIL DO JOGADOR", True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, 60))
        self.screen.blit(title, title_rect)
        
        # Botão voltar
        pygame.draw.rect(self.screen, BLUE, self.back_button)
        back_text = self.small_font.render("VOLTAR", True, WHITE)
        back_text_rect = back_text.get_rect(center=self.back_button.center)
        self.screen.blit(back_text, back_text_rect)
        
        # Botões de seção
        for i, (button, section) in enumerate(zip(self.section_buttons, self.sections)):
            color = GREEN if i == self.current_section else BLUE
            pygame.draw.rect(self.screen, color, button)
            pygame.draw.rect(self.screen, WHITE, button, 2)
            
            section_text = self.small_font.render(section, True, WHITE)
            section_text_rect = section_text.get_rect(center=button.center)
            self.screen.blit(section_text, section_text_rect)
        
        # Conteúdo da seção
        if self.current_section == 0:
            self.draw_statistics()
        elif self.current_section == 1:
            self.draw_achievements()
        else:
            self.draw_history()
    
    def draw_statistics(self):
        player_data = self.player_reg.get_current_player_data()
        if not player_data:
            return
        
        # Informações do jogador
        info_y = 200
        info_spacing = 30
        
        infos = [
            f"Usuário: {self.player_reg.current_player}",
            f"Email: {player_data['email']}",
            f"Conta criada: {player_data['created_at'][:10]}",
            f"Último login: {player_data['last_login'][:10]}",
            "",
            f"Total de jogos: {player_data['total_games']}",
            f"Pontuação total: {player_data['total_score']}",
            f"Melhor pontuação: {player_data['highest_score']}",
            f"Tempo total jogado: {player_data['total_playtime']} segundos",
            f"Pontuação média: {player_data['total_score'] // max(1, player_data['total_games'])}"
        ]
        
        for info in infos:
            if info == "":
                info_y += 20
                continue
            text_surface = self.small_font.render(info, True, WHITE)
            self.screen.blit(text_surface, (50, info_y))
            info_y += info_spacing
    
    def draw_achievements(self):
        player_data = self.player_reg.get_current_player_data()
        if not player_data:
            return
        
        # Conquistas disponíveis
        achievements = [
            ("Primeiro Jogo", "Complete seu primeiro jogo", player_data['total_games'] >= 1),
            ("Destruidor", "Destrua 10 asteroides", player_data['total_score'] >= 10),
            ("Veterano", "Jogue 10 partidas", player_data['total_games'] >= 10),
            ("Mestre", "Atinga 100 pontos", player_data['highest_score'] >= 100),
            ("Lendário", "Atinga 500 pontos", player_data['highest_score'] >= 500),
            ("Viciado", "Jogue por 1 hora", player_data['total_playtime'] >= 3600),
            ("Perfeccionista", "Complete 50 jogos", player_data['total_games'] >= 50),
            ("Campeão", "Atinga 1000 pontos", player_data['highest_score'] >= 1000)
        ]
        
        y = 200
        for title, description, unlocked in achievements:
            color = GREEN if unlocked else (100, 100, 100)
            status = "✓ DESBLOQUEADO" if unlocked else "🔒 BLOQUEADO"
            
            # Título da conquista
            title_surface = self.font.render(title, True, color)
            self.screen.blit(title_surface, (50, y))
            
            # Descrição
            desc_surface = self.small_font.render(description, True, WHITE)
            self.screen.blit(desc_surface, (50, y + 25))
            
            # Status
            status_surface = self.small_font.render(status, True, color)
            self.screen.blit(status_surface, (50, y + 45))
            
            y += 80
        
        # Progresso geral
        unlocked_count = sum(1 for _, _, unlocked in achievements if unlocked)
        progress_text = f"Conquistas desbloqueadas: {unlocked_count}/{len(achievements)}"
        progress_surface = self.font.render(progress_text, True, YELLOW)
        self.screen.blit(progress_surface, (50, 500))
    
    def draw_history(self):
        player_data = self.player_reg.get_current_player_data()
        if not player_data:
            return
        
        # Histórico de jogos (simulado)
        history_y = 200
        history_title = self.font.render("Histórico de Jogos", True, WHITE)
        self.screen.blit(history_title, (50, history_y))
        history_y += 40
        
        # Simular histórico (em um sistema real, isso viria de um banco de dados)
        if player_data['total_games'] > 0:
            for i in range(min(10, player_data['total_games'])):  # Mostrar últimos 10 jogos
                game_num = player_data['total_games'] - i
                score = max(1, player_data['highest_score'] - (i * 5))  # Simular pontuações
                
                game_text = f"Jogo #{game_num}: {score} pontos"
                game_surface = self.small_font.render(game_text, True, WHITE)
                self.screen.blit(game_surface, (50, history_y))
                history_y += 25
        else:
            no_games_text = self.small_font.render("Nenhum jogo jogado ainda!", True, (150, 150, 150))
            self.screen.blit(no_games_text, (50, history_y)) 