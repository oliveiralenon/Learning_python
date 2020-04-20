"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número
inteiro) e o programa vai informar quantas cédulas de cada valor
serão entregues.

OBS: Considere que o caixa possui cédulas de RS50, R$20, R$10 e R$1.
"""
print('-=' * 20)
print('             Banco LENON')
print('-=' * 20)
valor = int(input('Que valor você deseja sacar? R$'))
notas50 = valor // 50
valor = valor - (notas50 * 50)
notas20 = valor // 20
valor = valor - (notas20 * 20)
notas10 = valor // 10
valor = valor - (notas20 * 10)
notas01 = valor // 1
valor = valor - (notas20 * 1)
print(f'Total de {notas50} cédulas de R$50')
print(f'Total de {notas20} cédulas de R$20')
print(f'Total de {notas10} cédulas de R$10')
print(f'Total de {notas01} cédulas de R$1')
print('-=' * 20)
print('Volte sempre!')
