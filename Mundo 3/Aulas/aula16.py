"""
Aula 16: Tuplas

- Variáveis compostas

len(lanche) = mostra quantos elementos tem dentro da variável lanche
---------------------------
tipos de variáveis compostas:
lanche = (tupla) [lista] {dicionário}
----------------------------

Tuplas são imutáveis, não é possível modificar espaços posteriormente

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')# pode colocar sem parêntese que irá dar certo para tuplas
for comida in lanche:
    print(f'Eu vou comer {comida}')


lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')# pode colocar sem parêntese que irá dar certo para tuplas
print(len(lanche)) # mostra resultado 4 (numero de elementos em lanche)


lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')# pode colocar sem parêntese que irá dar certo para tuplas
for cont in range(0, len(lanche)):
    print(lanche[cont])

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')# pode colocar sem parêntese que irá dar certo para tuplas
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')


lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')# pode colocar sem parêntese que irá dar certo para tuplas
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')# pode colocar sem parêntese que irá dar certo para tuplas
print(sorted(lanche)) #sorted coloca em ordem alfabética

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5)) #Diz quantas vezes aparece o número 5 em c.

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(8)) #Em que posição está o 8

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(5, 1)) # Busca a posição do número 5, a partir da posição 1

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) #del apaga a tupla inteira
print(pessoa)



n = 1, 2, 3, 4, 5
for c in n:
    print(c, end=' ')


"""

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
