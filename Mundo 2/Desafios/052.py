"""
Faça um programa que leia um número inteiro e diga
se ele é ou não um número primo.
"""

n = int(input('Digite um número inteiro: '))
contador = 0
for i in range(2, n):
    if (n % i == 0):
        print(f'Múltiplo de {i}')
        contador = contador + 1
if contador == 0:
    print(f'Número {n} é primo')
else:
    print(f'Número {n} não é primo pois tem {contador} múltiplo(s) acima de 2.')
