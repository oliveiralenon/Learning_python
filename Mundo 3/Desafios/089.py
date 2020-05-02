"""
Crie um programa que leia o nome e duas notas de
vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de
cada um e permita que o usuário possa mostra as
notas de cada aluno individualmente.
"""
lista = []
while True:
    nome = str(input('Qual o nome do aluno? ')).strip().title()
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    media = (n1 + n2) / 2
    lista.append([[nome, [n1, n2], media]])
    cod = str(input('Você deseja continuar? [S/N] ')).strip().upper()[0]
    while cod not in 'NS':
        cod = str(input('Você deseja continuar? [S/N] ')).strip().upper()[0]
    if cod == 'N':
        break
print('-=' * 15)
print(f'{"No.":<5}{"Nome":^10}{"Média":^10}  ')
for i in range(0, len(lista)):
    print(f'{i:<5}{lista[i][0][0]:^10}{lista[i][0][2]:^10}')
while True:
    aluno = int(input('Mostras a notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        break
    print(f' Notas de {lista[aluno][0][0]} são {lista[aluno][0][1]}')
print('------Volte sempre------')
