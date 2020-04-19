"""
Faça um programa que leia um número qualquer e mostre
o seu fatorial.

EX: 5! = 5 x 4 x 3 x 2 x 1 = 120

"""

num = int(input('Digite um número inteiro: '))
fat = 1
c = num
print(f'Calculando {num}! = ', end='')
while num >= 1:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat = fat * num
    num -= 1
    c -= 1
print(f'{fat}')