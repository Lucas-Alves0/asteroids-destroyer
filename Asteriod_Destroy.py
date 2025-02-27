import pygame
from pygame import *
from Game_Classes import *
from random import *


pygame.init()
tela = display.set_mode([840, 480])
display.set_caption('GameProject')

# Sprite(personagem)
objectGroup = sprite.Group()
asteroidGroup = sprite.Group()
shotGroup = sprite.Group()
scoreGroup = sprite.Group()

bg = sprite.Sprite(objectGroup)
bg.image = image.load(r"C:\Users\lucas.paula_kovi\VSCodeProjects\MyOwnProjects\asteroids_destroy\game_assets\data\Cenario.png")
bg.image = transform.scale(bg.image, [840, 480])
bg.rect = bg.image.get_rect()

player = MainPlayer(objectGroup)

# Music
mixer.music.load(r"C:\Users\lucas.paula_kovi\VSCodeProjects\MyOwnProjects\asteroids_destroy\game_assets\data\GameMusic.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.2)

# Sounds
shoot = mixer.Sound(r"C:\Users\lucas.paula_kovi\VSCodeProjects\MyOwnProjects\asteroids_destroy\game_assets\data\Shoot.wav")


gameloop = True
gameover = False
timer = 20
clock = time.Clock()

while gameloop:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            gameloop = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE and not gameover:
                shoot.play()
                shot = Shot(objectGroup, shotGroup)
                shot.rect.center = player.rect.center

    if not gameover:
        objectGroup.update()

        timer += 1
        if timer > 30:
            timer = 0
            if random() < 0.3:
                newAsteroid = Asteroid(objectGroup, asteroidGroup)

        collisionsPlayer = sprite.spritecollide(player, asteroidGroup, False, sprite.collide_mask)

        if collisionsPlayer:
            print('Game Over!')
            gameover = True

        hit = sprite.groupcollide(shotGroup, asteroidGroup, True, True, sprite.collide_mask)

    objectGroup.draw(tela)
    display.update()
