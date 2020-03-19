"""Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto"""
produto = float(input('Digite o preço do produto: R$'))
print('O preço com 5% de desconto é: R${0:.2f}'.format(produto * 0.95))
