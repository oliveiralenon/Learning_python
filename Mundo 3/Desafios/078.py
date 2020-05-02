"""
Faça um programa que leia 5 valores numéricos e guarde-os
em uma lista.

No final, mostre qual foi o maior e menor valor digitado
e as suas respectivas posições na lista.
"""
v = list()
for i in range(0, 5):
    v.append(int(input('Digite um número inteiro: ')))
print(f'O maior valor é {max(v)} e encontra-se nas posições ', end='')
for i, j in enumerate(v):
    if j == max(v):
        print(i, end=' ')
print(f'\nO menor valor é {min(v)} e encontra-se nas posições ', end='')
for i, j in enumerate(v):
    if j == min(v):
        print(i, end=' ')
