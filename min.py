import pygame
import random
from useful import*
from time import sleep

pygame.init()
x = 0
y = 0
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
walk = UP
a1 = sort()
a2 = sort()

win  = pygame.display.set_mode((600, 600))

pygame.display.set_caption('Snake')
minh = [(200, 200), (200, 210),  (200 , 220), (200, 230)]
skin = pygame.Surface((10, 10))
skin.fill((100, 212, 30))
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))
while True:
    pygame.time.delay(100)
    pygame.display.flip()
    win.fill((255, 255, 255))
    a = False
    font = pygame.font.Font(None, 50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        walk = LEFT
        a = True
    if keys[pygame.K_RIGHT]:
        walk = RIGHT
        a = True
    if keys[pygame.K_UP]:
        walk = UP
        a = True
    if keys[pygame.K_DOWN]:
        walk = DOWN
        a = True

    if walk == LEFT:
        minh[0] = (minh[0][0] - 10, minh[0][1])
        a = True
    if walk == RIGHT:
        minh[0] = (minh[0][0] + 10, minh[0][1])
        a = True
    if walk == UP:
        minh[0] = (minh[0][0], minh[0][1] - 10)
        a = True
    if walk == DOWN:
        minh[0] = (minh[0][0], minh[0][1] + 10)
        a = True

    if minh[0][0] == 0:
        text = 'You lost'
        texto = font.render(text, True, (0, 0, 0))
        win.blit(texto, (250, 250))
        sleep(2)
        a1 = sort()
        a2 = sort()
        win = pygame.display.set_mode((600, 600))
        win.fill((255, 255, 255))
        pygame.display.set_caption('Snake')
        minh = [(200, 200), (200, 210), (200, 220), (200, 230)]
        skin = pygame.Surface((10, 10))
        skin.fill((100, 212, 30))
        apple = pygame.Surface((10, 10))
        apple.fill((255, 0, 0))
    if minh[0][0] == 600:
        win.fill((0, 0, 0))
        skin.fill((0, 0, 0))
        text = 'You lost'
        texto = font.render(text, True, (0, 0, 0))
        win.blit(texto, (250, 250))
        sleep(2)
        a1 = sort()
        a2 = sort()
        win = pygame.display.set_mode((600, 600))
        win.fill((255, 255, 255))
        pygame.display.set_caption('Snake')
        minh = [(200, 200), (200, 210), (200, 220), (200, 230)]
        skin = pygame.Surface((10, 10))
        skin.fill((100, 212, 30))
        apple = pygame.Surface((10, 10))
        apple.fill((255, 0, 0))
    if minh[0][1] == 0 :
        text = 'You lost'
        texto = font.render(text, True, (0, 0, 0))
        win.blit(texto, (250, 250))
        win.fill((0, 0, 0))
        skin.fill((0, 0, 0))
        sleep(2)
        a1 = sort()
        a2 = sort()
        win = pygame.display.set_mode((600, 600))
        win.fill((255, 255, 255))
        pygame.display.set_caption('Snake')
        minh = [(200, 200), (200, 210), (200, 220), (200, 230)]
        skin = pygame.Surface((10, 10))
        skin.fill((100, 212, 30))
        apple = pygame.Surface((10, 10))
        apple.fill((255, 0, 0))
    if minh[0][1] == 600:
        win.fill((0, 0, 0))
        skin.fill((0, 0, 0))
        text = 'You lost'
        texto = font.render(text, True, (0, 0, 0))
        win.blit(texto, (250, 250))
        sleep(2)
        a1 = sort()
        a2 = sort()
        win = pygame.display.set_mode((600, 600))
        win.fill((255, 255, 255))
        pygame.display.set_caption('Snake')
        minh = [(200, 200), (200, 210), (200, 220), (200, 230)]
        skin = pygame.Surface((10, 10))
        skin.fill((100, 212, 30))
        apple = pygame.Surface((10, 10))
        apple.fill((255, 0, 0))

    for cont in range(len(minh)-1, 0, -1):
        if minh[0][0] == minh[cont][0] and minh[0][1] == minh[cont][1]:
            win.fill((0, 0, 0))
            skin.fill((0, 0, 0))
            sleep(2)
            a1 = sort()
            a2 = sort()
            win = pygame.display.set_mode((600, 600))
            win.fill((255, 255, 255))
            pygame.display.set_caption('Snake')
            minh = [(200, 200), (200, 210), (200, 220), (200, 230)]
            skin = pygame.Surface((10, 10))
            skin.fill((100, 212, 30))
            apple = pygame.Surface((10, 10))
            apple.fill((255, 0, 0))

    if comun(minh[0], (a1, a2)):
        a1 = sort()
        a2 = sort()
        minh.append((0, 0))

    if a == True:
        for i in range(len(minh) -1, 0, -1):
            minh[i] = (minh[i-1][0], minh[i-1][1])

    win.fill((255, 255, 255))
    win.blit(apple, (a1, a2))
    for pos in minh:
        win.blit(skin, pos)
    pygame.display.update()


