import pygame
import sys

class Retangulos_Brancos(pygame.Rect):
    def __init__(self, pos, tam):
        super().__init__(pos, tam)


class Cobra:
    def __init__(self, tela):
        self.tela = tela
        self.partes = []
        for c in range(0, 5):
            self.partes.append(Retangulos_Brancos([200, 200+20*c], [10, 10]))

    def mostrar(self):
        for c in self.partes:
            pygame.draw.rect(self.tela, (0, 0, 0), c)


pygame.init()

tela = pygame.display.set_mode([400, 400])
pygame.display.set_caption('Jogo da Cobra')
tempo = pygame.time.Clock()

rec = Cobra(tela)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    tela.fill((255, 255, 255))

    rec.mostrar()




    pygame.display.update()
    tempo.tick(30)
