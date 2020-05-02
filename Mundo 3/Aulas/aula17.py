"""
Estruturas compostas: Listas []

Listas são mutáveis (podem ser modificadas)

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']

lanche.append['cookie] #adiciona um item extra na lista lanche
lanche = ['hamburguer', 'suco', 'pizza', 'pudim', 'cookie']

lanche.insert(0, 'cachorro quente') #adiciona um novo item na posição 0
lanche = ['cachorro quente', 'hamburguer', 'suco', 'pizza',
'pudim', 'cookie']

del.lanche[3] #remove o elemento no item 3
lanche.pop(3) #método pop elimina o último elemento, mas se indicar a posição, serve também
lanche.remove('pizza') #remove o item que tem a string 'pizza'

if 'pizza' in lanche:
    lanche.remove('pizza') #com esse if só irá remover a pizza se tiver dentro de lanche,
     #pq se não tivesse, ocorreria erro.

valores = list(range(4,11)) #cria uma lista valores com 4, 5, 6, 7, 8, 9, 10

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort() #Deixa os valore sem ordem [0, 2, 3, 4, 5, 8, 9]
valores.sort(reverse=True) #deixa na ordem decrescente [9, 8, 5, 4, 3, 2, 0]
len(valores) = 7  #mostra tamanho da lista


------------------------------ prática -----------------------
num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 0)
print(num)
num.pop()  # exclui o último elemento da lista
print(num)
num.pop(2)  # exclui o elemento que está na posição 2
print(num)
num.remove(2)  # remove o primeiro valor 2 encontrado na lista
# (se nao tiver o 2, irá dar erro) é bom usar o IF nesse caso
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)


valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}!')
print('Cheguei ao final da lista.')


valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: '))) # Adiciona pelo teclado!!!

for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}!')
print('Cheguei ao final da lista.')


a = [2, 3, 4, 7]
b = a[:]  # b recebe uma cópia de todos valores de a
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')

L = [0, 1, 2, 3, 4]
2 in L
True  # resultado que irá gerar

for x in L:
    print(x)

L.insert(POS, x) # Acrescenta um valor x na posição POS

L.count(2) # Conta quantas vezes aparece o valor 2

L.index(9) # Mostra em qual posição encontra-se o primeiro número 9

L.remove(2) # Remove o primeiro número 2 que aparecer

L.pop(POS) # Remove item na posição(POS) de índice especificada

del L[POS] # Remove item na posição de índice especificada.

del L[i:j] # Remove os itens da posição i até a posição j

L[i] = valor # Muda o valor que existia na posição i da lista

L2 = [x + 1, for x in L] Cria a lista L2 com os elementos de L incrementados

L3 = [x ** 10 for x in L] Cria uma lista L3 com os elementos elevados na 10

len(L) = Retorna o tamanho da lista

list(L) = Retorna os elementos da lista

L.clear() = limpa toda a lista

sum(L) = soma todos elementos da lista L

map(f, lista) Aplica a função f a cada um dos elementos da lista;
para ver o resultado combine com list()
ex:
import math
list(map(math.sqrt, L))

l += [7]   #Adiciona a lista [7] no final da lista L

valores = [1, 2, 3, 4, 5, 5, 10]
print(valores[2:]) # percorre da posição 2 até o fim

valores[::-1] # inverte a lista
valores[::2]# percorre a lista pulando 1 número
print(*valores[::2]) # o '*' retira os [] do print final
"""
valores = [1, 2, 3, 4, 5, 5, 10]
print(*valores[::2])

