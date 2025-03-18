# Asteroid Destroyer

Asteroid Destroyer é um jogo simples desenvolvido em Python utilizando a biblioteca Pygame. O objetivo do jogo é controlar uma nave espacial e destruir asteroides enquanto evita colisões.

## Estrutura e Arquivos do Projeto

 - Asteriod_Destroy.py
 - Game_Classes.py
 - game_assets
    - Asteroid.png
    - Cenario.png
    - GameMusic.mp3
    - Spaceship_move0.png
    - Shoot.wav


## Requisitos

- Python 3.x
- Pygame
- Random

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

1. Execute o script [Asteriod_Destroy.py](http://_vscodecontentref_/3):
    ```sh
    python Asteriod_Destroy.py
    ```
2. Use as teclas `W` e `S` para mover a nave espacial para cima e para baixo.
3. Pressione a barra de espaço para atirar nos asteroides.
4. Evite colidir com os asteroides. Se colidir, o jogo termina.

## Estrutura do Código

- [Asteriod_Destroy.py](http://_vscodecontentref_/4): Script principal que inicializa o jogo, gerencia o loop do jogo e trata os eventos.
- [Game_Classes.py](http://_vscodecontentref_/5): Contém as classes
    - [MainPlayer](http://_vscodecontentref_/6)
    - [Asteroid](http://_vscodecontentref_/7)
    - [Shot](http://_vscodecontentref_/8) que definem os comportamentos dos sprites do jogo.
- `game_assets/data/`: Diretório contendo os arquivos de imagem e som utilizados no jogo.

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
