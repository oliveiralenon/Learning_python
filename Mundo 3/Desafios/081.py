"""
Crie um programa que vai ler vários números e colocar
em uma lista. Depois disso, mostre:
a) quantos números foram digitados.
b) A lista de valores, ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista,
"""
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    cod = str(input('Você deseja continuar? [S/N]')).upper().strip()[0]
    while cod not in 'SN':
        cod = str(input('Você deseja continuar? [S/N]')).upper().strip()[0]
    if cod == 'N':
        break
print(f'A lista tem um total de {len(lista)} números.')
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')
if lista.count(5) == 0:
    print('A lista não tem valor 5.')
else:
    print(f'O Valor 5 faz parte da lista.')
