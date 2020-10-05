from pygame import *
import sys
import pygame

pygame.init()
tela = pygame.display.set_mode([600, 600])

tempo = pygame.time.Clock()

ret = pygame.Rect(20, 20, 50, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ret.x = ret.x - 10
            if event.key == pygame.K_RIGHT:
                ret.x = ret.x + 10
            if event.key == pygame.K_UP:
                ret.y = ret.y - 10
            if event.key == pygame.K_DOWN:
                ret.y = ret.y + 10

    tela.fill((255, 255, 255))


    pygame.draw.rect(tela, (255, 0, 0), ret)

    pygame.display.update()

    tempo.tick(30)
