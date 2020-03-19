"""
Escreva um programa que pergunte a quantidade
de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o
carro custa R$60 por dia e R$0,15 por Km
rodado.

"""

dias = float(input('Quantos dias alugado? '))
km = int(input('Quantos km rodados? '))
s = (km * 0.15) + (dias * 60)
print(f'Valor total a pagar: R${s:.2f}')
