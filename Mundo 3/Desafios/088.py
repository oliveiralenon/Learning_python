"""
Faça um programa que ajude um jogador da mega sena
a criar palpites. O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre 1
e 60 para cada jogo, cadastrando tudo em uma lista
composta.
"""
from random import sample
from time import sleep

lista = []
cod = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*5, 'Sorteando!!', '-='*5)
for i in range(0, cod):
    aposta = sample(range(1, 61), 6)
    lista.append(aposta)
    lista[i].sort()
    print(f'{i+1}º jogo: {lista[i]}')
    sleep(1)
print('-=' * 5, 'Boa sorte!!', '-=' * 5)
