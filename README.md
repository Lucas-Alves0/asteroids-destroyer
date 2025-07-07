# Asteroid Destroyer

Asteroid Destroyer é um jogo simples desenvolvido em Python utilizando a biblioteca Pygame. O objetivo do jogo é controlar uma nave espacial e destruir asteroides enquanto evita colisões.

## Estrutura do Projeto

```
assets/
  background/
    Cenario.png
  enemies/
    Asteroid.png
  ships/
    Spaceship_move0.png
    spaceship_concepts.png
  shoot/
    Shot.png
    Shot_1.png
  sounds/
    GameMusic.mp3
    Shoot.wav
  ui/
    start_button.png
    exit_button.png
src/
  asteroid.py
  game_manager.py
  leaderboard.py
  menu.py
  network.py
  player.py
  save_state.py
  shot.py
  ui.py
  utils.py
main.py
config.py
README.md
```

## Requisitos

- Python 3.x
- Pygame

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/asteroid-destroy.git
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd asteroid-destroy/MyOwnProjects/asteroids_destroy
    ```
3. Instale as dependências:
    ```sh
    pip install pygame
    ```

## Como Jogar

1. Execute o script principal:
    ```sh
    python main.py
    ```
2. Use as teclas `W` e `S` para mover a nave espacial para cima e para baixo.
3. Pressione a barra de espaço para atirar nos asteroides.
4. Evite colidir com os asteroides. Se colidir, o jogo termina.

## Estrutura do Código

- `main.py`: Script principal que inicializa o jogo, gerencia o loop do jogo e trata os eventos.
- `src/`: Contém os módulos do jogo:
    - `player.py`: Define o jogador e seu comportamento.
    - `asteroid.py`: Define os asteroides e seu comportamento.
    - `shot.py`: Define os tiros e seu comportamento.
    - `game_manager.py`: Gerencia o estado do jogo.
    - `ui.py`: Elementos de interface.
    - Outros módulos auxiliares.

## Melhorias Futuras

- Menus (inicial, pausa, configurações, loja, leaderboard, scoreboard)
- Salvamento e auto-salvamento
- Novos tipos de inimigos e power-ups
- Animações aprimoradas

## Contribuição

1. Faça um fork do projeto.
2. Crie uma nova branch:
    ```sh
    git checkout -b minha-nova-funcionalidade
    ```
3. Faça suas alterações e commit:
    ```sh
    git commit -am 'Adiciona nova funcionalidade'
    ```
4. Envie para o repositório remoto:
    ```sh
    git push origin minha-nova-funcionalidade
    ```
5. Abra um Pull Request.
