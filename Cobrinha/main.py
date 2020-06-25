import pygame
import sys

pygame.init()

tela = pygame.display.set_mode([400, 400])
pygame.display.set_caption('Jogo da Cobra')
tempo = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    tela.fill((255, 255, 255))
    pygame.display.update()
    tempo.tick(30)
