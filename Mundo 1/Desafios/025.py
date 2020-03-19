"""
Crie um programa que leia o nome de uma pessoa e diga se
ela tem "SILVA" no nome.
"""
nome = str(input('Digite seu nome completo: ')).strip()
split = nome.split()
silva = 'Silva' in nome[0:].title()
print(f'No nome {nome}, existe o sobrenome Silva? {silva} ')
