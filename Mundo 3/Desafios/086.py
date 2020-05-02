"""
Crie um programa que crie uma matriz de dimensão
3x3 e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela, com a formatação correta.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor ({l} x {c}): '))
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')  # :^5 deixa com cinco espaços e centralizado.
    print()

"""lista = [[], [], []]
coluna = 0
linha = 0
for i in range(0, 9):
    n = int(input(f'Digite o valor ({coluna} x {linha}): '))
    if coluna == 0:
        lista[0].append(n)
        linha += 1
    elif coluna == 1:
        lista[1].append(n)
        linha += 1
    elif coluna == 2:
        lista[2].append(n)
        linha += 1
    if linha == 3:
        coluna += 1
        linha = 0
print('=-' * 20)
print(lista[0][0], lista[0][1], lista[0][2])
print(lista[1][0], lista[1][1], lista[1][2])
print(lista[2][0], lista[2][1], lista[2][2])
"""
