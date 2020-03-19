"""
Crie um algoritmo que leia um número e mostre
o seu dobro, triplo e raiz quadrada.
"""
n = float(input('Digite um número: '))
print(f'O dobro é: {n * 2}\nO triplo é: {n * 3}\nA raiz quadrada é: {n ** (1 / 2):.2f}')

#print(f'{n} {n-1}') <-- nova forma de usar o .format()