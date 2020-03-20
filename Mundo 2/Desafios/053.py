"""
Crie um programa que leia um frase qualquer e diga
se ela é um palíndromo, desconsiderando os espaços.
"""
frase = str(input('Digite uma frase: ')).lower()
contrario = frase[::-1]
if frase == contrario:
    print(f'A frase é um palíndromo.\nFrase: {frase}\nFrase ao ontrário: {contrario}')
else:
    print(f'A frase não é um palíndromo.\nFrase: {frase}\nFrase ao Contrário: {contrario}')
