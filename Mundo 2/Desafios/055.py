"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre
qual foi o maior e o menor peso lidos.
"""

for i in range(0, 5):
    p = float(input(f'Digite o peso (kg) da {i+1}ª pessoa: '))
    if i == 0:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        elif p < menor:
            menor = p
print(f'O menor peso é {menor}Kg\nO maior peso é {maior}Kg')
