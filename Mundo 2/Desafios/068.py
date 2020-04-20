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
    escolha = str(input('PAR OU ÍMPAR? [P/I] ')).upper().strip()
    pc = randint(1, 10)
    soma = n + pc
    if escolha == 'P':
        if soma % 2 == 0:
            cont += 1
            print('Você ganhou!')
            print(f'Você escolheu {n} e o computador escolheu {pc}. Total de {soma} deu PAR.')
            print('Vamos jogar novamente...')
            print('=-' * 10)
        else:
            print('Você perdeu!!')
            print(f'Você escolheu {n} e o computador escolheu {pc}. Total de {soma} deu ÍMPAR.')
            print('=-' * 10)
            print(f'GAME OVER! Você venceu {cont} vezes')
            break
    if escolha == 'I':
        if soma % 2 != 0:
            cont += 1
            print('Você ganhou!')
            print(f'Você escolheu {n} e o computador escolheu {pc}. Total de {soma} deu ÍMPAR.')
            print('Vamos jogar novamente...')
            print('=-' * 10)
        else:
            print('Você perdeu!!')
            print(f'Você escolheu {n} e o computador escolheu {pc}. Total de {soma} deu PAR.')
            print('=-' * 10)
            print(f'GAME OVER! Você venceu {cont} vezes')
            break
