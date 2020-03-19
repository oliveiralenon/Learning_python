"""
A confederação Nacional de natação precida de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- até 9 anos : mirim
- até 14 anos: infantil
- até 19 anos: junior
- até 25 anos: senior
- acima de 25 anos: master
"""
from datetime import date

ano = date.today().year
nasc = int(input('Digite o ano de nascimento do atleta: '))
idade = ano - nasc
if idade <= 9:
    print(f'O atleta de {idade} anos está na categoria Mirim.')
elif 9 < idade <= 14:
    print(f'O atleta de {idade} anos está na categoria Infantil.')
elif 14 < idade <= 19:
    print(f'O atleta de {idade} anos está na categoria Junior.')
elif 19 < idade <= 25:
    print(f'O atleta de {idade} anos está na categoria Sênior.')
elif idade > 25:
    print(f'O atleta de {idade} anos está na categoria Master.')
