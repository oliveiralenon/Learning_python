"""
Fala um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e
tangente desse ângulo.
"""
import math
ang = float(input('Digite o ângulo: '))
rad = math.radians(ang)
print(ang)
print(f'O seno do ângulo {ang}° é {math.sin(rad):.2f}')
print(f'O cosseno do ângulo {ang}° é {math.cos(rad):.2f}')
print(f'A tangente do ângulo {ang}° é {math.tan(rad):.2f}')
