import pygame
from pygame import *
from Game_Classes import *
from random import *


pygame.init()
screen_size = [840, 480]
tela = display.set_mode(screen_size)
display.set_caption('GameProject')

# Sprite(personagem)
objectGroup = sprite.Group()
asteroidGroup = sprite.Group()
shotGroup = sprite.Group()

# Score Point (Player Score)

player_score = 0
level = 1

pygame.font.init()
fonte_1 = pygame.font.Font('freesansbold.ttf', 18)
fonte_2 = pygame.font.SysFont('arialblack', 26)
fontX = 7
fontY = 7

levelX = 750
levelY = 7

startX = 420
startY = 240

def show_score(x, y):
    score_img = fonte_1.render(f'Score: {str(player_score)}', True, [255, 255, 255])
    tela.blit(score_img, (x, y))

def show_level(x, y):
    level_img = fonte_1.render(f'Level: {str(level)}', True, [255, 255, 255])
    tela.blit(level_img, (x, y))

def start_msg(text, font, text_col, x, y):
    start_img = font.render(text, True, text_col)
    tela.blit(start_img, (x, y))

bg = sprite.Sprite(objectGroup)
bg.image = image.load(r"C:\Users\lucas.paula_kovi\VSCodeProjects\MyOwnProjects\asteroids_destroy\game_assets\data\Cenario.png")
bg.image = transform.scale(bg.image, screen_size)
bg.rect = bg.image.get_rect()

# Define game variables
start_game = False
difficult = 0
asteroid_speed = 1

player = MainPlayer(objectGroup)

# Sounds
mixer.music.load(r"C:\Users\lucas.paula_kovi\VSCodeProjects\MyOwnProjects\asteroids_destroy\game_assets\data\GameMusic.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.1)

shoot = mixer.Sound(r"C:\Users\lucas.paula_kovi\VSCodeProjects\MyOwnProjects\asteroids_destroy\game_assets\data\Shoot.wav")

gameloop = True
gameover = False
timer = 20
clock = time.Clock()

while gameloop:

    clock.tick(60)

    if start_game == False:
        start_msg('Press ESC to play', fonte_2, [255, 255, 255], 275, 226)

    else:
        mixer.music.set_volume(0.2)
        
        if not gameover:
            objectGroup.update()

            timer += 1
            if timer > 30:
                timer = 0
                if random() < 0.35:
                    newAsteroid = Asteroid(objectGroup, asteroidGroup, speed=asteroid_speed)

            collisionsPlayer = sprite.spritecollide(player, asteroidGroup, False, sprite.collide_mask)

            if collisionsPlayer:
                print('Game Over!')
                gameover = True

            hit = sprite.groupcollide(shotGroup, asteroidGroup, True, True, sprite.collide_mask)

            if hit:
                player_score += 1
                difficult += 1
                
            if difficult == 10:
                asteroid_speed += 1
                difficult = 0
                level += 1
                print('Dificuldade Aumentada!')

        objectGroup.draw(tela)

        # display score
        show_score(fontX, fontY)
        show_level(levelX, levelY)

    for event in pygame.event.get():
        if event.type == QUIT:
            gameloop = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                start_game = True
            if event.key == K_SPACE and not gameover and start_game == True:
                shoot.play()
                shot = Shot(objectGroup, shotGroup)
                shot.rect.center = player.rect.center

    display.update()
