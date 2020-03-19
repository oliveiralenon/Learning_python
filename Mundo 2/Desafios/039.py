"""
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

nasc = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
if idade == 18:
    print(f'Você tem ou irá fazer {idade} anos em {ano}, portanto você deve alistar-se esse ano.')
elif idade > 18:
    print(f'Você tem ou irá fazer {idade} anos em {ano}, portanto seu tempo de alistamento já passou {idade - 18} anos.')
else:
    print(f'Você ainda não completou 18 anos, faltam {18 - idade} anos para o seu alistamento.')
