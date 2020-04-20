"""
Crie um programa que leia vários números inteiros pelo
teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição d parada. No final, mostre
quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).
"""
cont = soma = 0
while True:
    n = int(input('Digite um valor inteiro (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} valores foi {soma}!')
