"""
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.

ex: Ana Maria de Souza
primeiro = Ana
último = Souza
"""
nome = str(input('Digite seu nome completo: ')).strip()
nome_s = nome.split()
print(f'Seu primeiro nome é {nome_s[0]}.\nE seu último nome último é {nome_s[-1]}.')
