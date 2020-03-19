"""
Estrutura de repetição -> FOR

for c in range(0,3):
    if moeda:
        pega
    passo
    pula
passo
pega
-------------------------

for c in range(6, 0, -1):
    print(c)
print('FIM')
#resp: 6 5 4 3 2 1
----------------------------

for c in range(0, 7, 2):
    print(c)
print('FIM')
#resp: 0 2 4 6
-------------------------------

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

--------------------------------

i = int(input('INÍCIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

resp:
0
2
4
6
8
10
FIM
---------------------------------

"""

s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n  #mesma coisa que s = s + n
print(s)
