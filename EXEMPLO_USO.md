# Exemplo de Uso - Asteroids Destroyer

Este guia demonstra como usar todas as funcionalidades do jogo melhorado.

## 🎯 Primeira Execução

### 1. Criar Conta
- Execute `python main.py`
- Na tela de login, clique em "CRIAR CONTA"
- Preencha:
  - **Nome de usuário**: 3-20 caracteres, apenas letras e números
  - **Email**: Formato válido (ex: usuario@email.com)
  - **Senha**: Mínimo 6 caracteres
  - **Confirmar senha**: Deve ser igual à senha
- Clique em "CRIAR CONTA"

### 2. Fazer Login
- Use o nome de usuário e senha criados
- Clique em "ENTRAR"

## 🎮 Menu Principal

Após o login, você verá o menu principal com:

### JOGAR
- Inicia uma nova partida
- Tutorial aparece nos primeiros 5 segundos
- Controles: W/S ou ↑/↓ para mover, ESPAÇO para atirar

### PERFIL
- **Estatísticas**: Informações pessoais e estatísticas de jogo
- **Conquistas**: Lista de conquistas desbloqueadas e bloqueadas
- **Histórico**: Últimos jogos (simulado)

### CONFIGURAÇÕES
- **Volume da Música**: Slider para ajustar volume da trilha sonora
- **Volume dos Efeitos**: Slider para sons de tiro e colisões
- **Dificuldade**: Fácil, Normal ou Difícil
- **Tela Cheia**: Ativar/desativar modo fullscreen
- **VSync**: Sincronização vertical

### RANKING
- **Melhores Pontuações**: Ranking por maior pontuação
- **Mais Jogos**: Ranking por total de partidas
- **Mais Tempo Jogado**: Ranking por tempo total

### SAIR
- Faz logout e volta para tela de login

## 🎯 Durante o Jogo

### Controles
- **W/S ou ↑/↓**: Mover nave para cima/baixo
- **ESPAÇO**: Atirar
- **ESC**: Voltar ao menu principal

### Objetivo
- Destrua asteroides para ganhar pontos
- Evite colidir com asteroides
- A dificuldade aumenta com o tempo
- Tente alcançar a maior pontuação possível

### Game Over
- Mostra pontuação final e level alcançado
- **JOGAR NOVAMENTE**: Inicia nova partida
- **MENU PRINCIPAL**: Volta ao menu

## 📊 Sistema de Estatísticas

O jogo rastreia automaticamente:
- **Total de jogos** jogados
- **Pontuação total** acumulada
- **Melhor pontuação** pessoal
- **Tempo total** jogado
- **Pontuação média** por jogo

## 🏆 Conquistas

Conquistas são desbloqueadas automaticamente:
- **Primeiro Jogo**: Complete seu primeiro jogo
- **Destruidor**: Destrua 10 asteroides
- **Veterano**: Jogue 10 partidas
- **Mestre**: Atinga 100 pontos
- **Lendário**: Atinga 500 pontos
- **Viciado**: Jogue por 1 hora
- **Perfeccionista**: Complete 50 jogos
- **Campeão**: Atinga 1000 pontos

## 💾 Dados Salvos

O jogo salva automaticamente em:
- **players.json**: Dados de todos os jogadores
- **leaderboard.json**: Ranking global

## 🔧 Configurações Avançadas

### Volume
- Ajuste o volume da música e efeitos sonoros
- As configurações são salvas por jogador

### Dificuldade
- **Fácil**: Asteroides mais lentos, menos frequentes
- **Normal**: Dificuldade padrão
- **Difícil**: Asteroides mais rápidos, mais frequentes

## 🎨 Interface

### Cores
- **Verde**: Ações positivas, botões principais
- **Azul**: Navegação, botões secundários
- **Vermelho**: Ações perigosas, game over
- **Amarelo**: Destaques, títulos
- **Roxo**: Informações especiais

### Feedback Visual
- Botões mudam de cor ao passar o mouse
- Mensagens de sucesso/erro aparecem temporariamente
- Jogador atual é destacado no ranking

## 🚀 Dicas de Jogo

1. **Comece devagar**: Aprenda os controles no tutorial
2. **Foque na precisão**: Cada tiro conta
3. **Mantenha distância**: Evite ficar muito perto dos asteroides
4. **Use o espaço**: Mova-se constantemente
5. **Pratique**: Quanto mais joga, melhor fica

## 🔒 Segurança

- Senhas são criptografadas com SHA-256
- Dados são validados antes de salvar
- Sistema protege contra dados corrompidos

## 🐛 Solução de Problemas

### Jogo não inicia
- Verifique se Python 3.x está instalado
- Instale Pygame: `pip install pygame`

### Erro de arquivo
- Verifique se todos os arquivos estão presentes
- Execute `python main.py` na pasta correta

### Problemas de som
- Verifique se os arquivos de som estão na pasta assets/sounds/
- Ajuste o volume nas configurações

### Dados perdidos
- Os arquivos players.json e leaderboard.json são criados automaticamente
- Não delete esses arquivos manualmente

---

**Divirta-se jogando Asteroids Destroyer! 🚀** 