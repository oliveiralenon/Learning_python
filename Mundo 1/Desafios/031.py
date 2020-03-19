"""
Desenvolva um programa que pergunte a distância de uma viagem
em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km
para viagens de até 200Km e R$0,45 para viagens mais longas.
"""
d = float(input('Digite a distância de viagem em Km: '))
if d <= 200:
    valor = d * 0.5
    print(f'A viagem de {d}Km custará R$ {valor:.2f}')
else:
    valor = d * 0.45
    print(f'A viagem de {d}Km custará R$ {valor:.2f}')
