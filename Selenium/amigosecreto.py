from random import sample


def esta_na_lista(lis, p):
    for l in lis:
        if l == p:
            return True
    return False


pessoas = []
a = ''
while a != 'sair':
    a = input("Digite um nome: ")
    pessoas.append(a)
pessoas.pop()
dici = {}
j = []
for c in pessoas:
    p = sample(pessoas, k=1)
    p = p[0]
    while esta_na_lista(j, p) or c == p:
        p = sample(pessoas, k=1)
        p = p[0]
    dici[c] = p
    j.append(p)
print('=-='*7)
for c, v in dici.items():
    print(f'{c:<8}  ->  {v}')
