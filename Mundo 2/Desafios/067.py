"""
Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número for negativo.
"""

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        print('Programa finalizado!')
        break
    else:
        print('-=' * 20)
        for i in range(1, 11):
            print(f'{n} x {i} = {n * i}')
    print('-=' * 20)
