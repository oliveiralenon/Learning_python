"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
from random import randint
from time import sleep

txt = 'Jogo de Jokenpô'
print('-=' * 30)
print(f'{txt.center(60)}')
print('-=' * 30)
n = int(input('1 - Pedra\n2 - Papel\n3- Tesoura\nFaça sua escolha: '))
pc = randint(1, 3)
print('Jo')
sleep(0.5)
print('Ken')
sleep(0.5)
print('Pô!!!')
sleep(0.5)
if n == 1:
    print('\nVocê escolheu Pedra.')
    if pc == 1:
        print(f'Sua escolha [Pedra] x [Pedra] Escolha do computador.\nEmpate!!! Pedra com pedra gera empate.')
    elif pc == 2:
        print(f'Sua escolha [Pedra] x [Papel] Escolha do computador.\nVocê perdeu!!! Papel ganha de pedra.')
    elif pc == 3:
        print(f'Sua escolha [Pedra] x [Tesoura] Escolha do computador.\nVocê ganhou!!! Pedra ganha de tesoura.')
elif n == 2:
    print('\nVocê escolheu Papel.')
    if pc == 1:
        print(f'Sua escolha [Papel] x [Pedra] Escolha do computador.\nVocê ganhou!!! Papel ganha de pedra. ')
    elif pc == 2:
        print(f'Sua escolha [Papel] x [Papel] Escolha do computador.\nEmpate!!! Papel com papel gera empate.')
    elif pc == 3:
        print(f'Sua escolha [Papel] x [Tesoura] Escolha do computador.\nVocê perdeu!!! Tesoura ganha de papel.')
elif n == 3:
    print('\nVocê escolheu Tesoura.')
    if pc == 1:
        print(f'Sua escolha [Tesoura] x [Pedra] Escolha do computador.\nVocê perdeu!!! Pedra ganha de tesoura.')
    elif pc == 2:
        print(f'Sua escolha [Tesoura] x [Papel] Escolha do computador.\nVocê ganhou!!! Tesoura ganha de papel.')
    elif pc == 3:
        print(f'Sua escolha [Tesoura] x [Tesoura] Escolha do computador.\nEmpate!!! Tesoura com tesoura gera empate.')
else:
    print('\033[1;31mO código digitado não é uma das opções.\033[m')
sleep(10)

print(teste)