"""
Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados
B) A soma dos valores da tercera coluna
C) O maior valor da segunda linha
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor ({l} x {c}): '))
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')  # :^5 deixa com cinco espaços e centralizado.
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}.')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')

"""
#Minha resolução:
#----------------

lista = [[], [], []]
coluna = linha = soma = soma3coluna = 0

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
for c in range(0, 3):
    for i in range(0, 3):
        if lista[c][i] % 2 == 0:
            soma += lista[c][i]
print(f'A soma de todos valores pares é {soma}.')
for c in range(0, 3):
    soma3coluna += lista[c][2]
print(f'A soma da terceira coluna é {soma3coluna}.')
for c in range(0, 3):
    if c == 0:
        maior = lista[1][0]
    elif lista[1][i] > maior:
        maior = lista[1][i]
print(f'O maior valor da segunda linha é {maior}.')
"""
