"""Faça um programa que leia a largura e a altura
de uma parede em metros, calcule sua área e a quantidade
de tinta necessária para pintá-la, sendo que
cada litro de tinta pinta uma área de 2m²"""

altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
a = altura * largura
print('A área da parede é {0}m² e são necessários {1} litros de tinta para pintá-la'.format(a, (a / 2)))
