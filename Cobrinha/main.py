import pygame
import sys


def muda_lugar(x, y, dir, obj):
    for c in obj:
        c.lugares_mudar.append([x, y, dir])


def direcoes_opostas(dir1, dir2):
    opostos = [['cima', 'baixo'], ['direita', 'esquerda']]
    for c in opostos:
        if dir1 == c[0] and dir2 == c[1]:
            return True
        elif dir1 == c[1] and dir2 == c[0]:
            return True
    return False

class Retangulos_Brancos(pygame.Rect):
    def __init__(self, pos, tam):
        super().__init__(pos, tam)
        self.direcao = 'cima'
        self.lugares_mudar = []

    def mover(self):
        if self.direcao == 'cima':
            self.y -= 5
        elif self.direcao == 'baixo':
            self.y += 5
        elif self.direcao == 'direita':
            self.x += 5
        elif self.direcao == 'esquerda':
            self.x -= 5

    def verifica_direcao(self):
        if len(self.lugares_mudar) > 0:
            if self.x == self.lugares_mudar[0][0] and self.y == self.lugares_mudar[0][1]:
                if not direcoes_opostas(self.direcao, self.lugares_mudar[0][2]):
                    self.direcao = self.lugares_mudar[0][2]
                self.lugares_mudar.pop(0)


class Cobra:
    def __init__(self, tela):
        self.tela = tela
        self.partes = []
        self.posx, self.posy = 0, 0
        for c in range(0, 5):
            self.partes.append(Retangulos_Brancos([190, 190+15*c], [15, 15]))

    def mostrar(self):
        for c in self.partes:
            pygame.draw.rect(self.tela, (0, 0, 0), c)

    def andar(self):
        for c in self.partes:
            c.verifica_direcao()
            c.mover()

    def mudar_direcoes(self, event):
        self.posx, self.posy = self.partes[0].x, self.partes[0].y
        if event.key == pygame.K_DOWN:
            muda_lugar(self.posx, self.posy, 'baixo', self.partes)
        elif event.key == pygame.K_UP:
            muda_lugar(self.posx, self.posy, 'cima', self.partes)
        elif event.key == pygame.K_RIGHT:
            muda_lugar(self.posx, self.posy, 'direita', self.partes)
        elif event.key == pygame.K_LEFT:
            muda_lugar(self.posx, self.posy, 'esquerda', self.partes)




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
        if event.type == pygame.KEYDOWN:
            rec.mudar_direcoes(event)
    tela.fill((255, 255, 255))

    rec.mostrar()
    rec.andar()



    pygame.display.update()
    tempo.tick(30)
