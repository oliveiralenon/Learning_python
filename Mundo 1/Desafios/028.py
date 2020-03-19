"""
Escreva um programa que faça o computador "pensar" em um
número inteiro entre 0 e 5 e faça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu
ou perdeu.
"""
from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número inteiro entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
n1 = randint(0, 5)
n2 = int(input('Digite um número: '))
print('Processando...')
sleep(2)
if n1 == n2:
    print(f'Parabéns, você acertou. A máquina escolheu o número {n1} e você o número {n2}.')
else:
    print(f'Ops, você errou. Eu escolhi o número {n1} e você o número {n2}')
