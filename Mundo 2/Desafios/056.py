"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:

- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres tem com menos de 20 anos.
"""
s = 0
velho = 0
m = 0
for i in range(0, 4):
    nome = str(input(f'\nDigite o nome da {i + 1}ª pessoa: '))
    idade = int(input(f'Digite a idade da {i + 1}ª pessoa: '))
    sexo = str(input(f'Digite o sexo da {i + 1}ª pessoa (M/F): ')).lower()
    s = s + idade
    if sexo == 'm':
        if idade > velho:
            velho = idade
            velho_nome = nome
    if sexo == 'f':
        if idade < 20:
            m = m + 1
media = s / 4
print(f'A média de idade do grupo é {media:.1f} anos')
print(f'O nome do homem mais velho é {velho_nome.title()}.')
print(f'Existem {m} mulheres com menos de 20 anos.')