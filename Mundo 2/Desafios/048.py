"""
Faça um programa que calcule a soma entre todos os
número ímpares que são múltiplos de três e que se
encontram no intervalo de 1 até 500.
"""
s = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s = i + s
print(f'A soma entre os números ímpares múltiplos de três entre (1 e 500) é: {s}')
