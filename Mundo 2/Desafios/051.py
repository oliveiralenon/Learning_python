"""
Desenvolva um programa que leia o primeiro termo e a
razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão.
"""

x = int(input('Escolha o primeiro termo da PA: '))
y = int(input('Escolha a razão da PA: '))
print('Progressão aritmética:')
for i in range(0, 10):
    pa = x + (i * y)
    print(pa, end=' -> ')
print('FIM')
