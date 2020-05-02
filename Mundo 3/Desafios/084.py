"""
Faça um programa que leia o nome e peso de várias
pessoas, guardando tudo em uma lista. No final, mostre:

a) Quantas pessoas foram cadastradas.

b) Uma listagem com as pessoas mais pesadas

c) uma listagem com as pessoas mais leves

"""

lista = []
dados = []
pesados = []
leves = []

cod = 'S'
while True:
    if cod == 'S':
        lista.append(str(input('Digite o nome da pessoa: ')).title().strip())
        lista.append(float(input('Digite o peso da pessoa em KG:  ')))
        dados.append(lista[:])
        lista.clear()
        cod = str(input('Você deseja continuar? [S/N] ')).upper().strip()[0]
        while cod not in 'SN':
            cod = str(input('Você deseja continuar? [S/N] ')).upper().strip()[0]
    else:
        break
print(f'Foram cadastradas um total de {len(dados)} pessoas.')
for i in range(0, len(dados)):
    if i == 0:
        maior = dados[i][1]
        menor = dados[i][1]
    else:
        if dados[i][1] > maior:
            maior = dados[i][1]
        elif dados[i][1] < menor:
            menor = dados[i][1]
for i in range(0, len(dados)):
    if maior == dados[i][1]:
        pesados.append(dados[i][0])
    elif menor == dados[i][1]:
        leves.append(dados[i][0])
print(f'A pessoa mais pesada é {pesados}')
print(f'A pessoa mais leve é {leves}')
