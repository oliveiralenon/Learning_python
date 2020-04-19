"""
Melhore o jogo do DESAFIO 028 onde o computador vai
"pensar" em um número entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
"""
from random import randint
abertura = 'Jogo da adivinhação!'
print('-=' * 20)
print(abertura.center(40))
print('-=' * 20)
print('Sou seu computador, acabei de pensar em um número entre 0 e 10.')
num = int(input('Tente adivinhar: '))
numc = randint(0, 10)
cont = 1
while num != numc:
    print('Você errou, tente novamente.')
    num = int(input('Digite um número entre 0 e 10: '))
    cont += 1
print(f'Parabéns, você ganhou!! Você necessitou de um total de {cont} palpites para acertar.')
print(f'Você escolheu o número {num} e eu escolhi o número {numc}.')
