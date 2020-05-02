"""
Crie um programa onde o usuário possa digitar 7
valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em
ordem crescente.
"""
lista = [[], []]
for i in range(0, 7):
    n = int(input(f'Digite o {i + 1}º número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
print(f'Lista de pares: {lista[0]}')
lista[1].sort()
print(f'Lista de ímpares: {lista[1]}')
