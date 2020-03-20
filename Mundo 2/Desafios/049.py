"""
Refaça o desafio 009, mostrando a tabuada de um
número que o usuário escolher, só que agora utilizando
um laço FOR.
"""
n = int(input('Digite um número inteiro entre (1 e 10): '))
if 1 < n > 10:
    print('Número de tabuada inválido.')
else:
    print('-=' * 10)
    print(f'Tabuada do número {n}')
    print('-=' * 10)
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
