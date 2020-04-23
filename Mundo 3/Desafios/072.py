"""
Crie um programa que tenha uma tupla preenchida com uma
contagem por extenso, de zero até vinte.

Seu prograva deverá ler um número pelo teclado(entre 0 e
20) e mostrá-lo por extenso.

"""

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
       'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
       'treze', 'catorze', 'quinze', 'dezeseis', 'dezesete',
       'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    while n > 20 or n < 0:
        n = int(input('Tente novamente... Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {num[n]}.')
    cod = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if cod == 'N':
        break
    while cod != 'S' and cod != 'N':
        cod = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
print('Programa finalizado, volte sempre!')
