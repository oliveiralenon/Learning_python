"""
Crie um programa que vai ler vários números e colocar
em uma lista.

Depois disso, crie duas listas extras que vão conter
apenas os valores pares e os valores ímpares digitados,
respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
"""
lista = []
par = []
impar = []

while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Você deseja continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Você deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        for i in range(0, len(lista)):
            if lista[i] % 2 == 0:
                par.append(lista[i])
            else:
                impar.append(lista[i])
        break
print(f'Lista: {lista}')
print(f'Pares: {par}')
print(f'Ímpares: {impar}')
