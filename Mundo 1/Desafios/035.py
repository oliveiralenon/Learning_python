"""
Desenvolva um programa que leia o comprimento de três
retas e diga ao usuário se elas podem ou não formar
um triângulo.
"""
print('-=' * 20)
print('\t\tComprimento de retas')
print('-=' * 20)
r1 = float(input('Digite o primeiro comprimento: '))
r2 = float(input('Digite o segundo comprimento: '))
r3 = float(input('Digite o terceiro comprimento: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('As medidas digitadas podem formar um triângulo.')
else:
    print('As medidas digitas não podem formar um triângulo.')
