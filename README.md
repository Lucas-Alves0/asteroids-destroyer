# Asteroids Destroyer

Um jogo de tiro espacial inspirado no clássico Asteroids, com sistema completo de autenticação e interfaces modernas.

## 🚀 Funcionalidades

### Sistema de Autenticação
- **Registro de jogadores** com validação de dados
- **Login seguro** com senhas criptografadas
- **Perfis personalizados** com estatísticas detalhadas
- **Sistema de conquistas** desbloqueáveis

### Interface Moderna
- **Tela de login/registro** com campos interativos
- **Menu principal** com múltiplas opções
- **Tela de perfil** com estatísticas e conquistas
- **Configurações** com controles de volume e dificuldade
- **Ranking global** com diferentes categorias

### Jogo
- **Controles intuitivos**: W/S ou setas para mover, ESPAÇO para atirar
- **Sistema de níveis** com dificuldade progressiva
- **Sons e música** com controles de volume
- **Tutorial interativo** para novos jogadores
- **Sistema de pontuação** persistente

## 🎮 Como Jogar

1. **Primeira execução**: Crie uma conta no sistema
2. **Login**: Use suas credenciais para acessar o jogo
3. **Menu principal**: Escolha entre jogar, ver perfil, configurações ou ranking
4. **Jogo**: Destrua asteroides para ganhar pontos
5. **Objetivo**: Sobreviva o máximo possível e alcance a maior pontuação

## 📊 Sistema de Estatísticas

O jogo rastreia automaticamente:
- **Total de jogos** jogados
- **Melhor pontuação** pessoal
- **Tempo total** jogado
- **Pontuação média** por jogo
- **Conquistas** desbloqueadas

## 🏆 Sistema de Conquistas

Conquistas disponíveis:
- **Primeiro Jogo**: Complete seu primeiro jogo
- **Destruidor**: Destrua 10 asteroides
- **Veterano**: Jogue 10 partidas
- **Mestre**: Atinga 100 pontos
- **Lendário**: Atinga 500 pontos
- **Viciado**: Jogue por 1 hora
- **Perfeccionista**: Complete 50 jogos
- **Campeão**: Atinga 1000 pontos

## ⚙️ Configurações

- **Volume da música**: Controle o volume da trilha sonora
- **Volume dos efeitos**: Ajuste sons de tiro e colisões
- **Dificuldade**: Escolha entre Fácil, Normal ou Difícil
- **Tela cheia**: Ative/desative modo fullscreen
- **VSync**: Sincronização vertical

## 📈 Ranking Global

O jogo mantém rankings em diferentes categorias:
- **Melhores pontuações**: Ranking por maior pontuação
- **Mais jogos**: Ranking por total de partidas
- **Mais tempo jogado**: Ranking por tempo total

## 🛠️ Tecnologias

- **Python 3.x**
- **Pygame** para gráficos e sons
- **JSON** para persistência de dados
- **Hash SHA-256** para segurança de senhas

## 📁 Estrutura do Projeto

```
asteroids-destroyer/
├── assets/                 # Recursos gráficos e sonoros
├── src/                    # Código fonte
│   ├── auth_ui.py         # Interface de autenticação
│   ├── main_menu.py       # Menu principal
│   ├── profile_screen.py  # Tela de perfil
│   ├── settings_screen.py # Configurações
│   ├── leaderboard_screen.py # Ranking
│   ├── player_registration.py # Sistema de registro
│   └── ...                # Outros módulos do jogo
├── main.py                # Arquivo principal
├── config.py              # Configurações
├── players.json           # Dados dos jogadores
└── leaderboard.json       # Ranking global
```

## 🚀 Como Executar

1. **Instale Python 3.x**
2. **Instale Pygame**: `pip install pygame`
3. **Execute o jogo**: `python main.py`

## 💾 Dados Salvos

O jogo salva automaticamente:
- **players.json**: Dados de todos os jogadores registrados
- **leaderboard.json**: Ranking global de pontuações

## 🎯 Controles

- **W/S ou ↑/↓**: Mover nave
- **ESPAÇO**: Atirar
- **ESC**: Voltar ao menu (durante o jogo)
- **Mouse**: Navegar pelas interfaces

## 🔒 Segurança

- Senhas são criptografadas com SHA-256
- Validação de dados de entrada
- Proteção contra dados corrompidos

## 🎨 Interface

- Design moderno e intuitivo
- Cores consistentes e acessíveis
- Feedback visual para todas as ações
- Responsivo a diferentes resoluções

---

**Desenvolvido com ❤️ para proporcionar uma experiência de jogo completa e envolvente!**
