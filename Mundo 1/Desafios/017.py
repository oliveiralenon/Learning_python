"""
Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo, calcule
e mostre o comprimento da hipotenusa.
"""
from math import sqrt
grand = input('Digite a grandeza dos dados: ')
c_opo = float(input('Digite o valor do cateto oposto: '))
c_adj = float(input('Digite o valor do cateto adjacente: '))
hipot = sqrt((c_opo ** 2) + (c_adj ** 2))
print(f'A hipotenusa é {hipot:.2f} {grand}')

# hipot = math.hypot(co, ca)
