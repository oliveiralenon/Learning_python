"""
Listas (Parte 2)

dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])     Pedro
print(dados[1])     25


pessoas = list()
pessoas.append(dados[:]) #coloca a lista de dados dentro da lista pessoas


pessoas = [['Pedro', 24], ['Maria', 19], ['João', 32]] #listas dentro de outra lista

print(pessoas[0][0]) #Vai printar Pedro
print(pessoas[1][1]) #vai printar 19
print(pessoas[2][0]) #vai printar João
print(pessoas[1]) #vai printar ['Maria', 19]


teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])  # Importante colocar esse[:] se não dá erro
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0][0])  #vai mostrar João

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1])  #vai mostrar 13

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for pessoa in galera:
    print(pessoa[0])  # mostra só os nomes de cada lista que tem em galera
    print(pessoa[1])  # mostra só as idades

    OU

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')

"""

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])  # cria uma copia da lista dado na lista galera
    dado.clear()  # limpa a lista dado para a próxima rodada do for

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')