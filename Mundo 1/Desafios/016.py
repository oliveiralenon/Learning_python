"""
Crie um programa que leia um número real qualquer pelo teclado e mostre
na tela a sua porção inteira.
"""
from math import trunc
num = float(input('Digite um número real: '))
print(f'A porção inteia de {num} é {trunc(num)}')
