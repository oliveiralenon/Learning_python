"""
Crie um programa que leia o nome e o preço de vários produtos. O
programa deverá perguntar se o usuário vai continuar. No final, mostre:
A) QUal é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
"""
cont = soma = i = 0
print('--' * 10)
print('       Lojinha')
print('--' * 10)
while True:
    produto = str(input('Nome do produto: ')).strip().title()
    preco = float(input('Digite o preço: R$'))
    soma += preco
    if i == 0:
        menorp = preco
        menorn = produto
    else:
        if preco < menorp:
            menorp = preco
            menorn = produto
    i += 1
    if preco > 1000:
        cont += 1
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000')
print(f'O produto mais barato foi {menorn} que custa R${menorp:.2f}')