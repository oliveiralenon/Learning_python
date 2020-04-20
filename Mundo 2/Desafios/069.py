"""
Faça um programa que leia a idade e o sexo de várias pessoas. A cada
pessoa cadastrada, o programa deverá perguntar se o usuário quer ou
não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
"""
cont = mulher = homem = 0
while True:
    print('-' * 20)
    print(str('CADASTRE UMA PESSOA'))
    print('-' * 20)
    idade = int(input('Idade: '))
    if idade > 18:
        cont += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo == 'F':
            if idade < 20:
                mulher += 1
        elif sexo == 'M':
            homem += 1
    else:
        if sexo == 'F':
            if idade < 20:
                mulher += 1
        elif sexo == 'M':
            homem += 1
    print('-' * 20)
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
    if opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('===== FIM DO PROGRAMA =====')
print(f'Foram cadastradas um total de {cont} pessoas maiores de 18 anos.')
print(f'Foram cadastrados um total de {homem} homens.')
print(f'Foram cadastradas um total de {mulher} mulheres com menos de 20 anos.')
