"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só
será interrompido quando o jogador perder, mostrando o total de
vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint

cont = 0
print('=-' * 13)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 13)
while True:
    n = int(input('Digite um número: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('PAR OU ÍMPAR? [P/I] ')).upper().strip()[0]
    pc = randint(1, 10)
    soma = n + pc
    print(f'Você jogou {n} e o computador {pc}. Total de {soma} ', end='')
    print('deu PAR.' if soma % 2 == 0 else 'deu ÍMPAR.')
    if escolha == 'P':
        if soma % 2 == 0:
            cont += 1
            print('Você ganhou!')
            print('=-' * 10)
        else:
            print('Você perdeu!!')
            print('=-' * 10)
            break
    elif escolha == 'I':
        if soma % 2 != 0:
            cont += 1
            print('Você ganhou!')
            print('=-' * 10)
        else:
            print('Você perdeu!!')
            print('=-' * 10)
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você ganhou {cont} vezes.')
