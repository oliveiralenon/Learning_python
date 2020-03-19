"""
Faça um programa que leia um número de 0 a 9999 e mostre na
tela cada um dos digitos separados.

ex:
Digite um número: 1834

unidade: 4
dezena: 3
centena: 8
milhar: 1
"""

"""num = int(input('Digite um número de 0 a 9999: '))
print(f'Unidade = {num[3]}')
print(f'Dezena = {num[2]}')
print(f'Centena = {num[1]}')
print(f'Milhar = {num[0]}')"""

from math import trunc
num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num //10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade = {u}')
print(f'Dezena = {d}')
print(f'Centena = {c}')
print(f'Milhar = {m}')
