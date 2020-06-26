dir1 = 'baixo'
dir2 = 'cima'
opostos = [['cima', 'baixo'], ['direita', 'esquerda']]
for c in opostos:
    if dir1 == c[0] and dir2 == c[1]:
        print('iguais')
    elif dir1 == c[1] and dir2 == c[0]:
        print('iguais')
print('diferentes')
