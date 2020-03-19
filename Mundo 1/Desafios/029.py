"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite.
"""
v = float(input('Digite a velocidade do carro: '))
if v > 80:
    multa = (v - 80) * 7
    print(f'Você ultrapassou o limite de 80 km/h, sua multa por andar a {v} km/h é R$ {multa}')
else:
    print(f'Sua velocidade {v} km/h está dentro do limite permitido.')
