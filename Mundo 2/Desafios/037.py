"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual
será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""
n = int(input('Digite um numero inteiro: '))
print('Opções de conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal')
c = int(input('Digite o código de conversão: '))
if c == 1:
    print(f'O valor {n} em binário é {bin(n)[2:]}')
elif c == 2:
    print(f'O valor {n} em octal é {oct(n)[2:]}')
elif c == 3:
    print(f'O valor {n} em hexadecimal é {hex(n)[2:]}')
else:
    print('A opção de conversão digitada não é válida.')
