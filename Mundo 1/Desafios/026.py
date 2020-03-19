"""
Crie um programa que leia uma frase pelo teclado e mostre:

- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez
"""
frase = str(input('Digite uma frase: ')).strip().lower()
first = frase.find('a')
last = frase[::-1].find('a')
print('A letra a aparece {} vezes na frase.'.format(frase.lower().count('a')))
print(f'O primeiro a está na posição: {first + 1}')
print('O último a está na posição: {} '.format(frase.rfind('a')+1))
