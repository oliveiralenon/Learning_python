"""
O mesmo professor do desafio anterior quer sortear
a ordem de apresentação de trabalhos dos alunos. Faça
um programa que leia o nome dos quatros alunos e mostre
a ordem sorteada.
"""
from random import sample
a1 = input('Digite o nome do aluno: ')
a2 = input('Digite o nome do aluno: ')
a3 = input('Digite o nome do aluno: ')
a4 = input('Digite o nome do aluno: ')
lista = [a1, a2, a3, a4]
sorteio = sample(lista, k=4)
print(f'A ordem de apresentação é: {sorteio}')

#outro exemplo
#random.shuffle(lista)
#print(f'A ordem de apresentação será {lista})
