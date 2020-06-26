import pygame
import sys
from random import randint


def sair():
    pygame.quit()
    sys.exit()


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
    def __init__(self, pos, tam, dir):
        super().__init__(pos, tam)
        self.direcao = dir
        self.lugares_mudar = []
        self.velocidade = 5

    def mover(self):
        if self.direcao == 'cima':
            self.y -= self.velocidade
        elif self.direcao == 'baixo':
            self.y += self.velocidade
        elif self.direcao == 'direita':
            self.x += self.velocidade
        elif self.direcao == 'esquerda':
            self.x -= self.velocidade

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
            self.partes.append(Retangulos_Brancos([190, 190+15*c], [15, 15], 'cima'))

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


class Maca:
    def __init__(self, tela):
        self.tela = tela
        x, y = randint(0, 38), randint(0, 38)
        self.ret = pygame.Rect([10*x, 10*y], [15, 15])

    def mostrar(self):
        pygame.draw.rect(self.tela, [255, 0, 0], self.ret)

    def mudar_pos(self):
        self.ret.x = 10*randint(0, 38)
        self.ret.y = 10*randint(0, 38)


pygame.init()

tela = pygame.display.set_mode([400, 400])
pygame.display.set_caption('Jogo da Cobra')
tempo = pygame.time.Clock()

rec = Cobra(tela)
maca = Maca(tela)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair()
        if event.type == pygame.KEYDOWN:
            rec.mudar_direcoes(event)
    tela.fill((255, 255, 255))

    if maca.ret.colliderect(rec.partes[0]):
        maca.mudar_pos()
        direc = rec.partes[-1].direcao
        x = rec.partes[-1].x
        y = rec.partes[-1].y
        if direc == 'cima':
            y += 15
        elif direc == 'baixo':
            y -= 15
        elif direc == 'direita':
            x -= 15
        elif direc == 'esquerda':
            x += 15
        rec.partes.append(Retangulos_Brancos([x, y], [15, 15], direc))
        rec.partes[-1].lugares_mudar = rec.partes[-2].lugares_mudar.copy()

    rec.mostrar()
    rec.andar()
    maca.mostrar()


    pygame.display.update()
    tempo.tick(30)
    for n in range(len(rec.partes)):
        if n != 1 and n != 0:
            if rec.partes[0].colliderect(rec.partes[n]):
                sair()
    if rec.partes[0].x < 0 or rec.partes[0].x > 385 or rec.partes[0].y < 0 or rec.partes[0].y > 385:
        sair()
