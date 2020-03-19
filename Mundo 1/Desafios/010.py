"""Crie um programa que leia quanto dinheiro uma
pessoa tem na carteira e mostre quantos dólares ela
pode comprar. Considere US$ = R$ 4.84"""
valor = float(input('Digite quanto dinheiro existe na carteira: R$ '))
print('Você tem R${0} que equivalem a US${1:.2f}'.format(valor, valor / 4.84))
