"""
Um professor quer sortear um dos seus quatro alunos
para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escreendo o nome do escolhido.
"""
#from random import sample
#a1 = input('Digite o nome do aluno: ')
#a2 = input('Digite o nome do aluno: ')
#a3 = input('Digite o nome do aluno: ')
#a4 = input('Digite o nome do aluno: ')
#sorteio = sample([a1, a2, a3, a4], k=1)
#print(f' Quem irá apagar o quadro é o aluno: {sorteio}')


#outra solução:
from random import choice
a1 = input('Digite o nome do aluno: ')
a2 = input('Digite o nome do aluno: ')
a3 = input('Digite o nome do aluno: ')
a4 = input('Digite o nome do aluno: ')
lista = [a1, a2, a3, a4]
sorteio = choice(lista)
print(f'Quem irá apagar o quadro é o aluno {sorteio}.')