"""
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:
a) quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números pares.

"""
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))
n3 = int(input('Digite um número inteiro: '))
n4 = int(input('Digite um número inteiro: '))
v = (n1, n2, n3, n4)
print(f'Você digitou os valores: {v}')
print(f'O valor 9 aparece {v.count(9)} vezes.')
if 3 in v:
    print(f'O valor 3 aparece na {v.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram', end=' ')
for n in v:
    if n % 2 == 0:
        print(n, end=' ')
