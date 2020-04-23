"""
Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e
também indique o menor e o maior valor que estão na tupla.
"""

"""
n = tuple((randint(0, 10))for i in range(0, 5))
print('Os valores sorteados foram:', end=' ')
for i in range(0, 5):
    print(n[i], end=' ')
print(f'\n O maior número sorteado foi o {max(n)}.\nO menor número sorteado foi o {min(n)}.')
"""
from random import randint, sample

n = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print(f'Eu sorteei os valores {n}')
print(f'O maior número é {max(n)}.\nO menor número é {min(n)}.')
