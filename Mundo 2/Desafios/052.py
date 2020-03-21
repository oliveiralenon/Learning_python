"""
Faça um programa que leia um número inteiro e diga
se ele é ou não um número primo.
"""

n = int(input('Digite um número inteiro: '))
contador = 0
for i in range(1, n+1):
    if n % i == 0:
        print(f'\033[4;33m{i}\033[m', end=' ')
        contador = contador + 1
    else:
        print(f'\033[31m{i}\033[m', end=' ')
if contador == 2:
    print(f'\nNúmero {n} é primo, pois é dividido apenas por 1 ou ele mesmo.')
else:
    print(f'\nNúmero {n} não é primo pois tem {contador} múltiplo(s).')
