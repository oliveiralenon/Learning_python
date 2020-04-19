"""

Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os n primeiros elementos de uma sequência
de Fibonacci.

ex:
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""

qtd = int(input('Quantos elementos da sequência de Fibonacci você deseja visualizar? '))
i = 0
n1 = 0
n2 = 1
print('0 1', end=' ')
while i < qtd - 2:
    n3 = n1 + n2
    print(f'{n3}', end=' ')
    i += 1
    n1 = n2
    n2 = n3
