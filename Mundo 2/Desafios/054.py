"""
Crie um programa que leia o ano de nascimento de sete
pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores.
"""
from datetime import date
maior = 0
menor = 0
ano = date.today().year
for i in range(0, 7):
    nasc = int(input(f'Digite o ano de nascimento da {i+1}ª pessoa: '))
    if ano - nasc >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print(f'{maior} pessoas já atingiram ou irão atingir a maioridade no ano de {ano}.')
print(f'{menor} pessoas ainda não atingiram a maioridade em {ano}.')
