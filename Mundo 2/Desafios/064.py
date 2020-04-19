"""

Crie um programa que leia vários numeros inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o flag [numero 999 de parada])

"""
num = int(input('Digite um número: '))
soma = num
cont = 1
while num != 999:
    num = int(input('Digite outro número (digite 999 para parar): '))
    soma += num
    cont += 1
print(f'Foram digitados um total de {cont - 1} números, com um somatório de {soma - 999}.')
