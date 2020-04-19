"""

Refaça o desafio 051, lendo o primeiro termo e a razão
de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while.
"""
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
i = 0
while i < 10:
    pa = termo + (i * razao)
    print(pa, end=' -> ')
    i += 1
print('Fim!')