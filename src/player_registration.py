import json
import os
import hashlib
import re
from datetime import datetime
from config import *

class PlayerRegistration:
    def __init__(self):
        self.players_file = 'players.json'
        self.current_player = None
        self.load_players()
    
    def load_players(self):
        """Carrega a lista de jogadores do arquivo"""
        if not os.path.exists(self.players_file):
            self.players = {}
            self.save_players()
        else:
            try:
                with open(self.players_file, 'r', encoding='utf-8') as f:
                    self.players = json.load(f)
            except:
                self.players = {}
                self.save_players()
    
    def save_players(self):
        """Salva a lista de jogadores no arquivo"""
        with open(self.players_file, 'w', encoding='utf-8') as f:
            json.dump(self.players, f, indent=4, ensure_ascii=False)
    
    def hash_password(self, password):
        """Cria hash da senha"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def validate_email(self, email):
        """Valida formato do email"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_username(self, username):
        """Valida nome de usuário"""
        return len(username) >= 3 and len(username) <= 20 and username.isalnum()
    
    def validate_password(self, password):
        """Valida senha"""
        return len(password) >= 6
    
    def register_player(self, username, email, password):
        """Registra um novo jogador"""
        if not self.validate_username(username):
            return False, "Nome de usuário deve ter 3-20 caracteres e ser alfanumérico"
        
        if not self.validate_email(email):
            return False, "Email inválido"
        
        if not self.validate_password(password):
            return False, "Senha deve ter pelo menos 6 caracteres"
        
        if username in self.players:
            return False, "Nome de usuário já existe"
        
        if any(player['email'] == email for player in self.players.values()):
            return False, "Email já cadastrado"
        
        hashed_password = self.hash_password(password)
        
        self.players[username] = {
            'email': email,
            'password': hashed_password,
            'created_at': datetime.now().isoformat(),
            'last_login': datetime.now().isoformat(),
            'total_games': 0,
            'total_score': 0,
            'highest_score': 0,
            'total_playtime': 0,
            'achievements': [],
            'settings': {
                'music_volume': 0.5,
                'sfx_volume': 0.5,
                'difficulty': 'normal'
            }
        }
        
        self.save_players()
        return True, "Jogador registrado com sucesso!"
    
    def login_player(self, username, password):
        """Faz login do jogador"""
        if username not in self.players:
            return False, "Usuário não encontrado"
        
        hashed_password = self.hash_password(password)
        if self.players[username]['password'] != hashed_password:
            return False, "Senha incorreta"
        
        self.players[username]['last_login'] = datetime.now().isoformat()
        self.current_player = username
        self.save_players()
        return True, "Login realizado com sucesso!"
    
    def logout_player(self):
        """Faz logout do jogador"""
        self.current_player = None
    
    def get_current_player_data(self):
        """Retorna dados do jogador atual"""
        if self.current_player and self.current_player in self.players:
            return self.players[self.current_player]
        return None
    
    def update_player_stats(self, score, playtime):
        """Atualiza estatísticas do jogador"""
        if not self.current_player:
            return
        
        player_data = self.players[self.current_player]
        player_data['total_games'] += 1
        player_data['total_score'] += score
        player_data['total_playtime'] += playtime
        
        if score > player_data['highest_score']:
            player_data['highest_score'] = score
        
        self.save_players()
    
    def get_player_stats(self, username=None):
        """Retorna estatísticas do jogador"""
        if username is None:
            username = self.current_player
        
        if username and username in self.players:
            return self.players[username]
        return None 