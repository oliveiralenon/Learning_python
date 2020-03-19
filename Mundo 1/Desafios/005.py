"""
Faça um programa que leia um número inteiro
e mostre na tela o seu sucessor e seu antecessor.
"""
n = int(input('Digite um número inteiro: '))
s = n + 1
a = n - 1
print('O número {0} tem como antecessor {1} e sucessor {2}.'.format(n, a, s))
