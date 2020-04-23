"""
Crie um programa que tenha uma tupla única com nomes de
produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os
dados em forma tabular.
"""
compras = ('Caneta', 3.5, 'Lápis', 1.5, 'Estojo', 15.59,
           'Caderno', 12.50, 'Borracha', 2)
print('-' * 50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-' * 50)
i = 0
while True:
    if i > len(compras):
        break
    print('{:.<40}'.format(compras[i]), end='')
    i += 1
    print(f'R${compras[i]:>7.2f}')
    i += 1

